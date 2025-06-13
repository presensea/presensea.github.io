# converter.py
#
# A Python script to convert a Markdown file into a standalone HTML blog post
# by using an external template file.
#
# Dependencies:
#   - Python 3.x
#   - 'markdown' library (`pip install markdown`)
#
# --- DOCUMENTATION ---
#
# This script requires a 'template.html' file to be in the same directory.
# The template should contain placeholders like {TITLE}, {AUTHOR_NAME},
# {CURRENT_DATE}, and {HTML_BODY} which the script will replace with content.
#
# Usage from the command line:
#   python converter.py <input_markdown_file> [options]
#
# Example 1: Basic conversion
#   This command converts 'post.md' into 'blog_YYYY-MM-DD.html'.
#   It requires 'template.html' to be present.
#
#   python converter.py post.md
#
# Example 2: Specifying output file and author
#   This command converts 'my_article.md' into 'my_awesome_post.html'
#   with "Jane Doe" as the author.
#
#   python converter.py my_article.md -o my_awesome_post.html -a "Jane Doe"
#
# Example 3: Getting help
#   This command displays all available options and how to use them.
#
#   python converter.py -h
#
# --- SCRIPT CODE ---

import markdown
import os
import re
import argparse
from datetime import datetime

def create_html_from_markdown(md_file_path, template_path, output_html_path, author_name):
    """
    Reads a Markdown file and a template, converts the markdown to HTML,
    and injects it into the template to create the final blog post.

    Args:
        md_file_path (str): Path to the input Markdown file.
        template_path (str): Path to the HTML template file.
        output_html_path (str): Path where the output HTML file will be saved.
        author_name (str): The author's name to display in the post header.
    """
    try:
        # --- 1. Read the Markdown file content ---
        with open(md_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        print(f"Successfully read content from '{md_file_path}'.")

        # --- 2. Read the HTML template file ---
        with open(template_path, 'r', encoding='utf-8') as f:
            html_template = f.read()
        print(f"Successfully read template from '{template_path}'.")

        # --- 3. Extract the title from the first H1 header ---
        title_match = re.search(r'^#\s(.+)', markdown_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            # Remove the H1 from the body content so it's not duplicated
            body_content_md = markdown_content.replace(title_match.group(0), '', 1)
        else:
            title = "PreSenSea"
            body_content_md = markdown_content
            print("No H1 header found. Using default title 'PreSenSea'.")

        # --- 4. Convert Markdown body to HTML ---
        html_body = markdown.markdown(body_content_md, extensions=['fenced_code', 'tables'])
        print("Markdown content converted to HTML successfully.")

        # --- 5. Get the current date for display ---
        current_date_display = datetime.now().strftime("%B %d, %Y")
        iso_date = datetime.now().isoformat()

        # --- 6. Replace placeholders in the template ---
        final_html = html_template.replace('{TITLE}', title)
        final_html = final_html.replace('{AUTHOR_NAME}', author_name)
        final_html = final_html.replace('{CURRENT_DATE}', current_date_display)
        final_html = final_html.replace('{ISO_DATE}', iso_date)
        final_html = final_html.replace('{HTML_BODY}', html_body)

        # --- 7. Write the final HTML to the output file ---
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"Success! Your blog post has been created at: '{output_html_path}'")
        print(f"You can open this file directly in your web browser.")

    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found.")
        print("Please make sure both your markdown file and template.html exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a styled HTML blog post using a template.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  # Basic conversion (creates blog_YYYY-MM-DD.html, uses template.html)
  python %(prog)s my_post.md

  # Specify output file and author
  python %(prog)s my_post.md -o my_article.html -a "Jane Doe"
"""
    )
    
    parser.add_argument(
        "input_file",
        help="Path to the input Markdown file (e.g., 'post.md')."
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Path for the output HTML file. \nIf not provided, defaults to 'blog_YYYY-MM-DD.html'."
    )
    
    parser.add_argument(
        "-t", "--template",
        default="template.html",
        help="Path to the HTML template file. \n(Default: 'template.html')"
    )
    
    parser.add_argument(
        "-a", "--author",
        default="PreSenSea Project",
        help="Author's name to be displayed in the post. \n(Default: 'PreSenSea Project')"
    )

    args = parser.parse_args()

    # Determine the output file path
    if args.output:
        html_file = args.output
    else:
        current_date_for_filename = datetime.now().strftime("%Y-%m-%d")
        html_file = f"blog_{current_date_for_filename}.html"

    # Run the conversion process
    create_html_from_markdown(args.input_file, args.template, html_file, args.author)
