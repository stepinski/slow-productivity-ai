# Setting Up Your PyCon Lithuania Presentation

This guide will walk you through how to set up and use the Metropolis Beamer theme for your PyCon Lithuania presentation using Quarto.

## Prerequisites

1. Install [Quarto](https://quarto.org/docs/get-started/) on your system
2. Basic familiarity with Markdown
3. (Optional) Install the Quarto VS Code extension if you use VS Code

## Installation

### Step 1: Install the Metropolis Theme Extension

```bash
quarto add shafayetShafee/metropolis-beamer
```

### Step 2: Create Your Presentation Directory

```bash
mkdir pycon-lithuania-presentation
cd pycon-lithuania-presentation
```

### Step 3: Set Up Project Files

Create the following files in your project directory:

1. `presentation.qmd` - Your main presentation file
2. `custom.scss` - The custom stylesheet with PyCon Lithuania colors
3. Create an `images` folder and save the PyCon Lithuania logo there

### Step 4: Download the PyCon Logo

For your convenience, you can use one of the PyCon Lithuania logos from the images you shared. Save it as `images/pycon-lt-logo.png` in your project directory.

## Customizing Your Presentation

### Color Scheme

The template uses the official PyCon Lithuania colors based on the Lithuanian flag:

- Yellow: #f7c118
- Green: #006837
- Red: #bf212f

These colors are defined in the `custom.scss` file and can be modified if needed.

### Typography

The presentation uses Roboto as the primary font family for a clean, modern look. If you prefer a different font, you can modify the font definitions in the `custom.scss` file.

## Rendering Your Presentation

To render your presentation, run:

```bash
quarto render presentation.qmd
```

This will create an HTML presentation that you can view in any modern web browser.

## Creating PDF Version (for Backup)

It's always good to have a PDF backup of your presentation:

```bash
quarto render presentation.qmd --to pdf
```

## Tips for a Great Presentation

1. **Use the section slides**: Use the section slides (with class `.section-slide`) to divide your presentation into clear segments.

2. **Code formatting**: When showing Python code, use the proper syntax highlighting with triple backticks and the language identifier:

   ```python
   def example():
       return "This is formatted Python code"
   ```

3. **Stay consistent**: Use the provided color scheme consistently throughout your presentation for a professional look.

4. **Images**: Place all your images in the `images/` directory and reference them with relative paths.

5. **Presenter mode**: Use the presenter mode by pressing 'S' during your presentation to see your notes and upcoming slides.

## Troubleshooting

If you encounter issues:

1. Make sure you have the latest version of Quarto installed
2. Verify that the metropolis extension was installed correctly
3. Check the console for any error messages during rendering

For more help, refer to the [Quarto documentation](https://quarto.org/docs/presentations/) or the [metropolis-beamer GitHub repository](https://github.com/shafayetShafee/metropolis-beamer/).
