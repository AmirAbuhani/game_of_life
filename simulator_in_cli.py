# This is fifth module. The Conway's Game of Life simulation is running in cli
import argparse
from simulator import run_game


def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life simulation")
    parser.add_argument('--size', type=int, default=8, help='Size of the grid (default: 8)')
    parser.add_argument('--rounds', type=int, default=4, help='Number of rounds to simulate (default: 10)')
    args = parser.parse_args()

    run_game(size=args.size, rounds=args.rounds)


if __name__ == "__main__":
    main()
