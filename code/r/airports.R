# ==============================================================================
#    NAME: code/r/airports.R
#   INPUT: Warming data
# ACTIONS: Animates a plot showing the population and sample airports
#  OUTPUT: MP4 saved to disk
# RUNTIME: X
#  AUTHOR: Thomas D. Pellegrin <thomas@pellegr.in>
#    YEAR: 2023
# ==============================================================================

# ==============================================================================
# 0 Housekeeping
# ==============================================================================

# Clear the environment
rm(list = ls())

# Load the required libraries
library(gganimate)
library(ncdf4)
library(rnaturalearth)
library(sf)
library(showtext)
library(sysfonts)
library(tidyverse)
library(viridis)

# Start a script timer
start_time <- Sys.time()

# Import custom font
font_add_google(name = "Overlock",   family = "Overlock")
showtext_auto()

# Clear the console
cat("\014")

# ==============================================================================
# 1 Load the airport data
# ==============================================================================

# Sort by asc. traffic, create a new column for population/sample, parse coords.
df <- read_csv(file = "data/airports.csv", col_types  = c("ccncnnf")) |>
  arrange(traffic) |>
  mutate(bin = as.factor(ifelse(traffic >= 10^6, "Sample", "Population"))) |>
  st_as_sf(coords = c("lon", "lat"), crs = 4326)

# ==============================================================================
# 2 Build the maps of airports
# ==============================================================================

# Define the world object minus Antarctica
world <- ne_countries(scale = "medium", returnclass = "sf") |>
  subset(continent != "Antarctica")

# Build the base plot
p <- ggplot() +
  geom_sf(data = world, color = NA, fill = "lightgray") +
  scale_fill_viridis(
    breaks    = c(min(df$traffic), 10^6, max(df$traffic)),
    direction = -1L,
    labels    = c("1", "1M", "100M"),
    name      = "Passenger traffic (2019)",
    option    = "rocket",
    trans     = "sqrt"
  ) +
  theme_light() +
  theme(
    axis.text          = element_blank(),
    axis.ticks         = element_blank(),
    axis.title         = element_blank(),
    panel.background   = element_blank(),
    panel.border       = element_blank(),
    panel.grid         = element_blank(),
    plot.background    = element_rect(fill = "#202124", color = NA)
  )

# ==============================================================================
# 2.1 Build the population map of airports
# ==============================================================================

# Build the plot
p +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  theme(
    legend.background  = element_rect(fill = "#202124", color = NA),
    legend.key.width   = unit(2L, "cm"),
    legend.position    = "bottom",
    legend.spacing.y   = unit(0.1, "cm"),
    legend.text        = element_text(color = "white", size = 32L, family = "Overlock"),
    legend.title       = element_text(color = "white", size = 48L, family = "Overlock"),
    legend.title.align = .5,
  ) +
  guides(fill = guide_colorbar(title.position = "top", title.hjust = 0.5)) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = nrow(df), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/1_airports_population.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)

# ==============================================================================
# 2.2 Build the sample map of airports
# ==============================================================================

# Build the plot
p +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  theme(
    legend.background  = element_rect(fill = "#202124", color = NA),
    legend.key.width   = unit(2L, "cm"),
    legend.position    = "bottom",
    legend.spacing.y   = unit(0.1, "cm"),
    legend.text        = element_text(color = "white", size = 32L, family = "Overlock"),
    legend.title       = element_text(color = "white", size = 48L, family = "Overlock"),
    legend.title.align = .5,
  ) +
  guides(fill = guide_colorbar(title.position = "top", title.hjust = 0.5)) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = nrow(df[df$traffic >= 10^6, ]), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/2_airports_sample.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)

# ==============================================================================
# 2.3 Build the sample map of airports overlaid with NetCDF grid
# ==============================================================================

# Load sample NetCDF data
nc_file <- "data/cli/tas_6hrPlevPt_MPI-ESM1-2-HR_ssp126_r1i1p1f1_gn_201501010600-202001010000.nc"

# Open the NetCDF file
nc <- ncdf4::nc_open(
  filename  = nc_file,
  write     = FALSE,
  readunlim = FALSE
)

# Read the latitudinal and longitudinal bounds of each cell
nc_lat <- ncdf4::ncvar_get(nc = nc, varid = "lat_bnds") |> t() |> as.data.frame() |> rename(ymin = V1, ymax = V2)
nc_lon <- ncdf4::ncvar_get(nc = nc, varid = "lon_bnds") |> t() |> as.data.frame() |> rename(xmin = V1, xmax = V2)

# Recode the longitude vector from 0°-360° to -180°-180°
nc_lon <- ((nc_lon + 180L) %% 360L) - 180L

# Assemble the coordinates into a data frame
nc_df <- cbind(nc_lat, nc_lon)

# Rebuild the grid of all cells (73,728)
grid <- expand(nc_df, nesting(ymin, ymax), nesting(xmin, xmax))

# Load the sample airports
df_smp <- read_csv(file = "data/airports.csv", col_types  = c("ccncnnf")) |>
  filter(traffic >= 10^6) |>
  select(icao, lat, lon)

# Find cells that overlap airports (823)
match <- lapply(
  X   = as.vector(df_smp$icao),
  FUN = function(x) {
    which.min(
      abs((grid$ymin + grid$ymax) / 2 - df_smp[df_smp$icao == x, ]$lat) +
        abs((grid$xmin + grid$xmax) / 2 - df_smp[df_smp$icao == x, ]$lon)
    )
  }
) |> unlist() |> unique()

# Sample airports with no grid overlay
p +
  coord_sf(expand = FALSE) +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  # Add the parallels
  geom_hline(
    color      = "green",
    # alpha      = .25,
    linewidth  = 0L,
    yintercept = unique(c(nc_lat$ymin, nc_lat$ymax))
  ) +
  # Add the meridians
  geom_vline(
    color      = "green",
    # alpha      = .25,
    linewidth  = 0L,
    xintercept = unique(c(nc_lon$xmin, nc_lon$xmax))
  ) +
  theme(
    legend.position = "none"
  ) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = nrow(df[df$traffic >= 10^6, ]), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/3_airports_sample_no_grid.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)

# Sample airports with grid overlay
p +
  coord_sf(expand = FALSE) +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  # Add the parallels
  geom_hline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    yintercept = unique(c(nc_lat$ymin, nc_lat$ymax))
  ) +
  # Add the meridians
  geom_vline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    xintercept = unique(c(nc_lon$xmin, nc_lon$xmax))
  ) +
  theme(
    legend.position = "none"
  ) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = nrow(df[df$traffic >= 10^6, ]), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/4_airports_sample_grid.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Sample airports with grid overlay and filled cells
p +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 2L, stroke = .1) +
  # Add the airports
  geom_rect(
    color   = NA,
    fill    = "green",
    linewidth = 0L,
    data    = data.frame(
      xmin  = grid[match, "xmin"],
      xmax  = grid[match, "xmax"],
      ymin  = grid[match, "ymin"],
      ymax  = grid[match, "ymax"]
    ),
    mapping = aes(
      xmin  = xmin,
      xmax  = xmax,
      ymin  = ymin,
      ymax  = ymax
    )
  ) +
  # Add the parallels
  geom_hline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    yintercept = unique(c(nc_lat$ymin, nc_lat$ymax))
  ) +
  # Add the meridians
  geom_vline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    xintercept = unique(c(nc_lon$xmin, nc_lon$xmax))
  ) +
  theme(
    legend.position = "none"
  ) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = length(match), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/5_airports_sample_grid_cells.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)

# Just the grid overlay and filled cells
p  +
  geom_sf(data = df[df$traffic < 10^6, ],  aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  geom_sf(data = df[df$traffic >= 10^6, ], aes(fill = traffic), shape = 21L, size = 0L, stroke = 0L) +
  # Add the airports
  geom_rect(
    color   = NA,
    fill    = "green",
    linewidth = 0L,
    data    = data.frame(
      xmin  = grid[match, "xmin"],
      xmax  = grid[match, "xmax"],
      ymin  = grid[match, "ymin"],
      ymax  = grid[match, "ymax"]
    ),
    mapping = aes(
      xmin  = xmin,
      xmax  = xmax,
      ymin  = ymin,
      ymax  = ymax
    )
  ) +
  # Add the parallels
  geom_hline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    yintercept = unique(c(nc_lat$ymin, nc_lat$ymax))
  ) +
  # Add the meridians
  geom_vline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    xintercept = unique(c(nc_lon$xmin, nc_lon$xmax))
  ) +
  theme(
    legend.position = "none"
  ) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = length(match), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/6_airports_sample_grid_cells.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)


# No map
p <- ggplot() +
  theme_light() +
  theme(
    axis.text          = element_blank(),
    axis.ticks         = element_blank(),
    axis.title         = element_blank(),
    panel.background   = element_blank(),
    panel.border       = element_blank(),
    panel.grid         = element_blank(),
    plot.background    = element_rect(fill = "#202124", color = NA)
  ) +
  # Add the airports
  geom_rect(
    color   = NA,
    fill    = "green",
    linewidth = 0L,
    data    = data.frame(
      xmin  = grid[match, "xmin"],
      xmax  = grid[match, "xmax"],
      ymin  = grid[match, "ymin"],
      ymax  = grid[match, "ymax"]
    ),
    mapping = aes(
      xmin  = xmin,
      xmax  = xmax,
      ymin  = ymin,
      ymax  = ymax
    )
  ) +
  # Add the parallels
  geom_hline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    yintercept = unique(c(nc_lat$ymin, nc_lat$ymax))
  ) +
  # Add the meridians
  geom_vline(
    color      = "green",
    # alpha      = .25,
    linewidth  = .04,
    xintercept = unique(c(nc_lon$xmin, nc_lon$xmax))
  ) +
  theme(
    legend.position = "none"
  ) +
  annotate(
    geom   = "text",
    x      = 0,
    y      = -55,
    label  = paste("n",  format(x = length(match), big.mark = ","), sep = " = "),
    size   = 24L,
    color  = "white",
    family = "Overlock"
  ) +
  coord_sf(expand = FALSE) # Remove the border around the map

# Save the plot
ggsave(
  filename = "out/7_just_grid_cells.png",
  plot     = last_plot(),
  height   = 2160L,
  width    = 3840L,
  units    = "px",
  dpi      = "retina",
  device   = "png",
  bg       = "#202124"
)

# ==============================================================================
# 3 Housekeeping
# ==============================================================================

# Stop the script timer
Sys.time() - start_time

# EOF