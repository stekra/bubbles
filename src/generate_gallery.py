import os

def generate_html(folder_path, output_file="output.html"):
    # Get a list of image files in the folder
    allowed_extensions = {"jpg", "jpeg", "png", "gif", "bmp", "webp"}
    image_files = [f for f in os.listdir(folder_path) if f.split('.')[-1].lower() in allowed_extensions]

    # Start building the HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <div class="grid">
"""

    # Add each image to the HTML content
    for idx, image_file in enumerate(image_files, start=1):
        img_path = os.path.join("imgs", image_file)  # Use relative path starting with 'imgs/'
        html_content += f"""
        <div class="item">
            <div id="img{idx}" class="img-container">
                <img src="{img_path}" alt="Image {idx}">
            </div>
        </div>
        """

    # Close the HTML structure
    html_content += """
    </div>
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' generated successfully with {len(image_files)} images.")

# Example usage
if __name__ == "__main__":
    folder = input("Enter the folder path containing images: ")
    folder = folder.strip()
    output_html = "gallery.html"
    generate_html(folder, output_html)
