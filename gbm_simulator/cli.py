from gbm_simulator import GBMSimulator
import matplotlib.pyplot as plt
import argparse

def simulate(y0, mu, sigma, T, N, output):
    simulator = GBMSimulator(y0, mu, sigma)
    t, Y = simulator.simulate_path(T, N)

    #plot results
    plt.plot(t, Y)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Geometric Brownian Motion')

    plt.savefig(output)
    return t, Y

def main():
    """
    Main function for the CLI tool.
    """
    parser = argparse.ArgumentParser(description="GBM CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command for displaying company info
    parser_info = subparsers.add_parser("simulate", help="Simulate GBM")
    parser_info.add_argument("--y0", type=float, required=True, help="Initial position (stock price).")
    parser_info.add_argument("--mu", type=float, required=True, help="Drift.")
    parser_info.add_argument("--sigma", type=float, required=True, help="Volatility.")
    parser_info.add_argument("--T", type=float, required=True, help="Time horizon.")
    parser_info.add_argument("--N", type=int, required=True, help="Number of steps.")
    parser_info.add_argument("--output", type=str, required=True, help="Output file name.")


    args = parser.parse_args()

    if args.command == "simulate":
        simulate(args.y0, args.mu, args.sigma, args.T, args.N, args.output)


if __name__ == "__main__":
    main()