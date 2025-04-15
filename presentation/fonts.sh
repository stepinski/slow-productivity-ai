#!/bin/bash

# Create fonts directory
mkdir -p fonts

# Download the Google Fonts we need
echo "Downloading fonts..."

# Bebas Neue
curl -L "https://fonts.gstatic.com/s/bebasneue/v9/JTUSjIg69CK48gW7PXoo9Wlhyw.woff2" -o "fonts/bebas-neue-regular.woff2"

# Anton
curl -L "https://fonts.gstatic.com/s/anton/v23/1Ptgg87LROyAm3Kz-C8.woff2" -o "fonts/anton-regular.woff2"

# Oswald - Regular and Bold
curl -L "https://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs1_FvsUZiZQ.woff2" -o "fonts/oswald-regular.woff2"
curl -L "https://fonts.gstatic.com/s/oswald/v49/TK3_WkUHHAIjg75cFRf3bXL8LICs1xZosUZiZQ.woff2" -o "fonts/oswald-bold.woff2"

# Open Sans - Regular, Medium, Bold and Italic
curl -L "https://fonts.gstatic.com/s/opensans/v34/memvYaGs126MiZpBA-UvWbX2vVnXBbObj2OVTS-muw.woff2" -o "fonts/open-sans-regular.woff2"
curl -L "https://fonts.gstatic.com/s/opensans/v34/memvYaGs126MiZpBA-UvWbX2vVnXBbObj2OVTSKmu1aB.woff2" -o "fonts/open-sans-medium.woff2"
curl -L "https://fonts.gstatic.com/s/opensans/v34/memvYaGs126MiZpBA-UvWbX2vVnXBbObj2OVTSumu1aB.woff2" -o "fonts/open-sans-bold.woff2"
curl -L "https://fonts.gstatic.com/s/opensans/v34/memtYaGs126MiZpBA-UFUIcVXSCEkx2cmqvXlWqWtk6F15M.woff2" -o "fonts/open-sans-italic.woff2"

# Montserrat - Regular and Bold
curl -L "https://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Hw5aXo.woff2" -o "fonts/montserrat-regular.woff2"
curl -L "https://fonts.gstatic.com/s/montserrat/v25/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCuM73w5aXo.woff2" -o "fonts/montserrat-bold.woff2"

echo "All fonts downloaded successfully to the 'fonts' directory"
