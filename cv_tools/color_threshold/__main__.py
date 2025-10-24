"""
Command-line interface for Color Threshold Finder
"""

import argparse
import sys
from .color_threshold_finder import ColorThresholdFinder


def main():
    parser = argparse.ArgumentParser(
        description="Interactive HSV color threshold finder for images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s image.png
  %(prog)s image.png --mask --result
  %(prog)s image.png --all --output my_thresholds.txt
  
Controls:
  Q - Quit the application
  S - Save current thresholds to file
        """,
    )

    parser.add_argument(
        "image_path", type=str, metavar="image", help="Path to the input image"
    )

    parser.add_argument(
        "--show-image", "-i", action="store_true", help="Display original image window"
    )

    parser.add_argument(
        "--mask", "-m", action="store_true", help="Display binary mask window"
    )

    parser.add_argument(
        "--result", "-r", action="store_true", help="Display filtered result window"
    )

    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Display all windows (image, mask, and result)",
    )

    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="thresholds.txt",
        help="Output file path for saving thresholds (default: thresholds.txt)",
    )

    args = parser.parse_args()

    # Set display flags
    display_image = args.show_image or args.all
    display_mask = args.mask or args.all
    display_result = args.result or args.all

    # If no display flags are set, default to showing result
    if not (display_image or display_mask or display_result):
        display_result = True

    try:
        finder = ColorThresholdFinder(
            image_path=args.image_path,
            display_image=display_image,
            display_mask=display_mask,
            display_result=display_result,
            thresholds_path=args.output,
        )

        print(f"Loading image: {args.image_path}")
        print(f"Output file: {args.output}")
        print("\nControls:")
        print("  Q - Quit")
        print("  S - Save thresholds")
        print("\nAdjust trackbars to find optimal color thresholds...")

        finder.find_color_threshold()

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
