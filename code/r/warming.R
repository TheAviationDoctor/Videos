# ==============================================================================
#    NAME: code/r/warming.R
#   INPUT: Warming data
# ACTIONS: Animates a plot showing the surface temperature increase up to 2100
#  OUTPUT: Animation saved to disk
# RUNTIME: ~15 minutes
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
# 1 Load the temperature data
# ==============================================================================

df <- read_csv(
  file = "data/ssp.csv",
  col_types = "ifdddi"
)

# ==============================================================================
# 2 Plot the temperature data
# ==============================================================================

p <- ggplot(data = df[df$var != "SSP119", ]) +
  
  # Horizontal axis scale
  xlim(1950, 2115) +
  
  # Add degree sign to vertical axis
  scale_y_continuous(labels = ~ paste0(.x, "°C")) +
  
  # Rename axis labels
  labs(
    x = "Year",
    y = "Warming above the 1850–1900 average"
  ) +
  
  # Vertical separation line between historical and forecast
  geom_vline(
    xintercept = 2014.5,
    linetype   ="solid",
    color      = "white",
    linewidth  = 3L
  ) +
  
  # Top labels
  annotate(
    "text",
    x      = 1975,
    y      = 6,
    col    = "white",
    family = "Overlock",
    size   = 18L,
    label  = "Historical (1950–2014)"
  ) +
  annotate(
    "text",
    x      = 2056,
    y      = 6,
    col    = "white",
    family = "Overlock",
    size   = 18L,
    label  = "Forecast (2015–2099)"
  ) +
  
  # Uncertainty ribbon
  geom_ribbon(
    mapping    = aes(x = year, ymin = low, ymax = high, fill = var, group = var),
    alpha      = 0.1
  ) +
  
  # 5th percentile line
  geom_line(
    mapping    = aes(x = year, y = low, color = var, group = var),
    linewidth  = .25,
    alpha      = .25
  ) +
  
  # Mean line
  geom_line(
    mapping    = aes(x = year, y = mean, color = var, group = var),
    linewidth  = 2L
  ) +
  
  # 95th percentile line
  geom_line(
    mapping    = aes(x = year, y = high, color = var, group = var),
    linewidth  = .25,
    alpha      = .25
  ) +
  
  # Moving target lines
  geom_segment(
    aes(x = year, y = mean, xend = 2099, yend = mean),
    linetype = 2L,
    colour   = "white"
  ) +
  
  # Temperature label
  geom_text(
    mapping    = aes(
      x        = 2101,
      y        = mean,
      label    = paste(
        var, ": ",
        formatC(round(mean, digits = 1L), format="f", digits = 1L), "°C",
        sep    = ""
      ),
      color    = var
    ),
    hjust      = "left",
    family     = "Overlock",
    size       = 18L
  ) +
  
  # Adjust theme cosmetics
  theme(
    axis.line        = element_line(linewidth = 1L, linetype = "solid", color = "white"),
    axis.title       = element_text(color = "white"),
    axis.title.y     = element_text(margin = margin(t =  0L, r = 35L, b = 0L, l = 25L)),
    axis.text.x      = element_text(margin = margin(t = 10L, r =  0L, b = 0L, l = 0L), color = "white"),
    axis.text.y      = element_text(margin = margin(t =  0L, r = 10L, b = 0L, l = 0L), color = "white"),
    legend.position  = "none",
    panel.background = element_blank(),
    panel.border     = element_blank(),
    panel.grid       = element_blank(),
    plot.background  = element_rect(fill = "#202124", color = NA),
    text             = element_text(color = "white", family = "Overlock", size = 64L)
  )

# Show plot
p

# ==============================================================================
# 3 Animate the plot
# ==============================================================================

# Build the animation
a <- p + transition_reveal(along = seq, keep_last = TRUE)

# Render the animation
animate(
  plot        = a,
  duration    = 66L,
  fps         = 24L,
  renderer    = ffmpeg_renderer(),
  height      = 2160L,
  width       = 3840L,
  bg          = "#202124",
  end_pause   = 72L,
  start_pause = 72L
)

# Save the animation
anim_save(
  filename = "out/global-warming.mp4",
  animation = last_animation()
)