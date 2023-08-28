import os
import sys
import warnings

import numpy as np
import pandas as pd
from mizani.formatters import percent_format
from plotnine import *
from PIL import Image, ImageDraw, ImageFont

warnings.filterwarnings("ignore")

dataset = pd.read_csv('C:/Users/siu856309481/Downloads/Mean WVS + Econ by Country.csv')

plot = (
    ggplot(dataset, aes(x='reorder(B_COUNTRY_ALPHA, Mean_Q3)', y='Mean_Q3', fill ='Mean_Q3'))  # Note the '-' in '-Mean_Q3' to sort in descending order
    + geom_col()
    + ylab("Leisure")
    + xlab("Country")
    + coord_flip()
    + theme_bw()
    + theme(
        axis_title_x=element_text(size=15),
        axis_title_y=element_text(size=15),
        axis_text_x=element_text(size=9.5),
        axis_text_y=element_text(size=9.5),  # Adjust the font size to improve label visibility
        plot_title=element_text(hjust=0.5, size=20),  # Center the title
        legend_position = "right"
    )
    + scale_fill_gradient(name='Mean_Q3', low="lightsalmon", high="green")  # Gradient from light blue to deep blue
    + labs(y="Leisure", x="Country", title="Perceived importance of leisure")
    + guides(fill=guide_legend(title='Leisure'))

)

# Display the plot with increased height
plot.save('C:/Users/siu856309481/Downloads/output_plot.png', width=10, height=8, dpi = 500)

# Open the saved image using PIL
img = Image.open('C:/Users/siu856309481/Downloads/output_plot.png')

# Prepare to add text
draw = ImageDraw.Draw(img)
text = "Prepared by Promise Tewogbola. Source: World Values Survey"
font = ImageFont.truetype('arial.ttf', 50)  # Adjust the font and size as needed. You may need the path to the font.

# Compute the position to draw text at the bottom right
textwidth, textheight = draw.textsize(text, font)
# The -10 and -10 offsets ensure the text doesn't touch the image border
x = img.width - textwidth - 10
y = img.height - textheight - 10

# Draw the text onto the image
draw.text((x, y), text, font=font, fill="black")

# Save the image with the text
img.save('C:/Users/siu856309481/Downloads/output_plot.png')
