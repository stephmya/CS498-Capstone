import argparse
import os


def title_images(input_dir, prefix, digits=2, extension=None):
	if not os.path.isdir(input_dir):
		print(f"Input directory does not exist: {input_dir}")
		return

	normalized_extension = None
	if extension:
		normalized_extension = extension if extension.startswith(".") else f".{extension}"
		normalized_extension = normalized_extension.lower()

	files = [
		name
		for name in sorted(os.listdir(input_dir), key=str.lower)
		if os.path.isfile(os.path.join(input_dir, name))
		and (normalized_extension is None or os.path.splitext(name)[1].lower() == normalized_extension)
	]

	if not files:
		print("No matching files found.")
		return

	print(f"Renaming files in: {input_dir}")

	for index, old_name in enumerate(files, start=1):
		old_path = os.path.join(input_dir, old_name)
		new_name = f"{prefix}-{index:0{digits}d}{os.path.splitext(old_name)[1]}"
		new_path = os.path.join(input_dir, new_name)

		os.rename(old_path, new_path)
		print(f"Renamed: {old_name} -> {new_name}")


def main() -> None:
	parser = argparse.ArgumentParser(description="Rename files to a numbered prefix format.")
	parser.add_argument('--input_dir', default=None, help='Folder containing files to rename')
	parser.add_argument('--prefix', default='bollards_monaco_2', help='Prefix used before the number')
	parser.add_argument('--digits', type=int, default=2, help='Zero-padding digits')
	parser.add_argument('--ext', default=None, help='Only rename files with this extension (e.g. jpg)')
	args = parser.parse_args()

	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	default_input = os.path.join(base_dir, 'processing_data', 'monaco_2_bollards_raw')
	input_path = args.input_dir if args.input_dir else default_input

	title_images(input_path, args.prefix, args.digits, args.ext)


if __name__ == "__main__":
    main()
