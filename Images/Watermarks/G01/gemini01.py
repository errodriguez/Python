from PIL import Image

def remove_elements(image_path, output_path):
    """Removes the crayon and stars from the bottom right corner of an image.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output image.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Get the dimensions of the image
        width, height = img.size

        # Define the region to remove (bottom right corner)
        # Assuming the crayon and stars are within a 100x100 pixel square
        remove_region = (width - 100, height - 100, width, height)

        # Create a new image with the same dimensions as the original
        new_img = Image.new("RGBA", img.size)

        # Paste the original image onto the new image, excluding the region to remove
        new_img.paste(img.crop((0, 0, width - 100, height - 100)), (0, 0))
        new_img.paste(img.crop((width - 100, 0, width, height - 100)), (width - 100, 0))
        new_img.paste(img.crop((0, height - 100, width - 100, height)), (0, height - 100))

        # Save the new image
        new_img.save(output_path, "PNG")

        print(f"Elements removed and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
image_path = "image.png"  # Replace with the actual path to your image
output_path = "image_no_elements.png"
remove_elements(image_path, output_path)
