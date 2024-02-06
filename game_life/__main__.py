import sys

from game_life import patterns, views
from game_life.cli import get_command_line_args

def main():
    args = get_command_line_args()

    # Get the view class
    View = getattr(views, args.view)

    # Check to display all patterns or a specific pattern
    if args.all:
        # Display all available patterns
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        # Display a specific pattern 
        _show_pattern(
            View,
            patterns.get_pattern(name=args.pattern),
            args
        )

def _show_pattern(View, pattern, args):
    try:
        # Display the pattern using the specified view
        View(pattern=pattern, gen=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        # Handle errors and print them
        print(error, file=sys.stderr)

if __name__ == "__main__":
    main()