import argparse


def total_minutes(blocks, minutes):
    if blocks <= 0 or minutes <= 0:
        raise ValueError("Use positive numbers.")

    return blocks * minutes


def main():
    parser = argparse.ArgumentParser(
        description="Plan study time"
    )

    parser.add_argument(
        "--blocks",
        type=int,
        required=True
    )

    parser.add_argument(
        "--minutes",
        type=int,
        default=25
    )

    args = parser.parse_args()

    try:
        total = total_minutes(args.blocks, args.minutes)

    except ValueError as error:
        parser.error(str(error))

    print("Total minutes:", total)

    if total >= 60:
        print("Plan a break.")
    else:
        print("Short study session.")


if __name__ == "__main__":
    main()