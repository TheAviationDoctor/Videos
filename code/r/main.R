# ==============================================================================
#    NAME: code/r/main.R
#   INPUT: Population and sample airport data
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
library(av)
library(gganimate)
library(ggrepel)
library(rnaturalearth)
library(sf)
library(showtext)
library(sysfonts)
library(tidyverse)
library(transformr)
library(viridis)

# Start a script timer
start_time <- Sys.time()

# Import custom font
font_add_google(name = "Overlock", family = "Overlock")
showtext_auto()

# Clear the console
cat("\014")

# ==============================================================================
# 1 Plot of global warming by SSP
# ==============================================================================

# ==============================================================================
# 1.1 Load and transform the warming data
# ==============================================================================

df_cli <- read_csv(
  file = "data/warming.csv",
  col_select = c(1, 3, 6, 9, 12, 15),
  col_types = "iddddd"
) |> pivot_longer(
  cols = !Year,
  names_to = "var",
  names_transform = list(var = as.factor),
  values_to = "val",
  values_drop_na = TRUE
)

# Filter final year values for display
# df_end <- filter(df_cli, Year == max(Year))

# ==============================================================================
# 1.2 Build the base plot of global warming
# ==============================================================================

p <- ggplot(data = df_cli, aes(x = Year, y = val, group = var)) +
  geom_line(color = "white", linewidth = 2L) +
  geom_point(color = "#FF6961", size = 10L, alpha = .75) +
  geom_segment(aes(xend = 2108L, yend = val), linetype = 2L, colour = "white") +
  geom_text(
    aes(x = 2110L, label = formatC(round(val, digits = 1L), format="f", digits = 1L)),
    color = "white",
    size = 10L
  ) +
  labs(x = "Year", y = "Warming in °C") +
  theme(
    axis.line          = element_line(linewidth = 0.5, linetype = "solid", colour = "white"),
    axis.title.y       = element_text(margin = margin(t = 0L, r = 50L, b = 0L, l = 0L)),
    panel.background   = element_blank(),
    panel.border       = element_blank(),
    panel.grid         = element_blank(),
    plot.background    = element_rect(fill = "#202124", color = NA),
    text               = element_text(color = "white", family = "Overlock", size = 32L)
  )

# ==============================================================================
# 1.3 Animate the plot
# ==============================================================================

# Build the animation
anim_cli <- p +
  transition_reveal(along = Year, keep_last = TRUE)

# Render the animation
animate(
  plot      = anim_cli,
  duration  = 15L,
  fps       = 24,
  renderer  = av_renderer(),
  height    = 2160L,
  width     = 3840L,
  bg        = "#202124"
)

# Save the animation
anim_save(
  filename = "clips/WarmingPlot.mp4",
  animation = last_animation()
)

# # ==============================================================================
# # 2 World map of airports
# # ==============================================================================
# 
# # ==============================================================================
# # 2.1 Load and transform the airport data
# # ==============================================================================
# 
# df_apt <- read_csv(file = "data/airports.csv") |>
#   arrange(desc(traffic)) |>
#   st_as_sf(
#     coords = c("lon", "lat"),
#     crs = "+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0"
#   )
# 
# # ==============================================================================
# # 2.2 Build the plot of airports
# # ==============================================================================
# 
# # Define the world object minus Antarctica
# world <- ne_countries(scale = "medium", returnclass = "sf") |>
#   subset(continent != "Antarctica")
# 
# # Build the plot
# p <- ggplot() +
#   geom_sf(data = world, color = NA, fill = "lightgray") +
#   geom_sf(data = df_apt, aes(fill = traffic), shape = 21L, size = 7L, stroke = 1L) +
#   scale_fill_viridis(
#     breaks    = c(min(df_apt$traffic), max(df_apt$traffic)),
#     direction = -1L,
#     labels    = c("1", "10^8"),
#     option    = "rocket",
#     trans     = "sqrt"
#   ) +
#   guides(fill = guide_colorbar(title.position = "top")) +
#   labs(fill = "Passenger traffic in 2019") +
#   theme_light() +
#   theme(
#     axis.text          = element_blank(),
#     axis.ticks         = element_blank(),
#     axis.title         = element_blank(),
#     legend.background  = element_blank(),
#     legend.direction   = "horizontal",
#     legend.position    = c(.5, .1),
#     legend.key.height  = unit(1.5, "cm"),
#     legend.key.width   = unit(4L, "cm"),
#     legend.text        = element_text(size = 32L),
#     legend.title       = element_text(size = 32L),
#     legend.title.align = 0.5,
#     panel.background   = element_blank(),
#     panel.border       = element_blank(),
#     panel.grid         = element_blank(),
#     plot.background    = element_rect(fill = "#202124", color = NA),
#     text               = element_text(color = "white", family = "Overlock")
#   )
# 
# # Save the plot
# if(!file.exists("plots/MapOfAirports.png")) {
#   ggsave(
#     filename = "plots/MapOfAirports.png",
#     plot     = last_plot(),
#     height   = 2160L,
#     width    = 3840L,
#     units    = "px",
#     dpi      = 320L,
#     device   = "png",
#     bg       = "#202124"
#   )
# }
# 
# # ==============================================================================
# # 2.3 Animate population airports
# # ==============================================================================
# 
# # Build the animation
# anim_pop <- p +
#   transition_manual(frames = traffic, cumulative = TRUE)
# 
# # Render the animation
# animate(
#   plot      = anim_pop,
#   nframes   = length(unique(df_apt$traffic)),
#   fps       = 24L,
#   renderer  = av_renderer(),
#   height    = 2160L,
#   width     = 3840L,
#   bg        = "#202124"
# )
# 
# # Save the animation
# anim_save(
#   filename  = "videos/MapOfAirportsPopulation.mp4",
#   animation = last_animation()
# )
# 
# # ==============================================================================
# # 2.4 Animate sample airports
# # ==============================================================================
# 
# # Build the animation
# anim_smp <- p +
#   transition_filter(
#     transition_length = 5L,
#     filter_length     = 5L,
#     population_layer  = traffic >= 1L,
#     sample_layer      = traffic >= 10^6,
#     keep              = TRUE,
#     wrap              = FALSE
#   ) +
#   exit_shrink()
# 
# # Render the animation
# animate(
#   plot      = anim_smp,
#   duration  = 15L,
#   fps       = 24L,
#   renderer  = av_renderer(),
#   height    = 2160L,
#   width     = 3840L,
#   bg        = "#202124"
# )
# 
# # Save the animation
# anim_save(
#   filename = "videos/MapOfAirportsSample.mp4",
#   animation = last_animation()
# )
# 
# # ==============================================================================
# # 3 Sampling strategy
# # ==============================================================================
# 
# # ==============================================================================
# # 3.1 Load and transform the data
# # ==============================================================================
# 
# df_apt <- read_csv(file = "data/aerodromes.csv")
# 
# # ==============================================================================
# # 3.2 Build the plot
# # ==============================================================================
# 
# # p <- ggplot(data = df_apt, mapping = aes(x = reorder(category, -count), y = count)) +
# #   geom_col(position = "identity", fill = "#FF6961") +
# #   geom_text(
# #     mapping  = aes(label = trunc(count)),
# #       color  = "white",
# #       family = "Overlock",
# #       size   = 8L,
# #       vjust  = -1L
# #   ) +
# #   scale_y_continuous(limits = c(0, max(df_apt$count) * 1.05)) +
# #   theme_light() +
# #   theme(
# #     aspect.ratio       = 2160 / 3840,
# #     axis.text.x        = element_text(color = "white"),
# #     axis.text.y        = element_blank(),
# #     axis.ticks         = element_blank(),
# #     axis.title         = element_blank(),
# #     legend.position    = "none",
# #     panel.border       = element_blank(),
# #     panel.background   = element_blank(),
# #     panel.grid         = element_blank(),
# #     plot.background    = element_rect(fill = "#202124", color = NA),
# #     plot.margin        = margin(t = 1L, r = 1L, b = 1L, l = 1L, unit = "cm"),
# #     text               = element_text(family = "Overlock", size = 32L)
# #   )
# # 
# # p
# # 
# # # ==============================================================================
# # # 3.3 Animate the plot
# # # ==============================================================================
# # 
# # # Build the animation
# # anim_apt <- p +
# #   # transition_states(states = time, transition_length = 10L, state_length = 1L, wrap = FALSE) +
# #   transition_time(time = time)
# #   ease_aes("sine-in-out")
# # 
# # # Render the animation
# # animate(
# #   plot      = anim_apt,
# #   # duration  = 15L,
# #   fps       = 10,
# #   renderer  = av_renderer(),
# #   height    = 2160L / 3,
# #   width     = 3840L / 3, 
# #   bg        = "#202124"
# # )
# # 
# # 
# # 
# # 
# # # Save the animation
# # anim_save(
# #   filename = "videos/SamplingStrategy.mp4",
# #   animation = last_animation()
# # )

# ==============================================================================
# 4 Housekeeping
# ==============================================================================

# Stop the script timer
Sys.time() - start_time

# EOF