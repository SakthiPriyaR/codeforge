import argparse
import sys
import traceback

from agent.graph import agent


def main():
    parser = argparse.ArgumentParser(description="CodeForge: turn a prompt into a working project")
    parser.add_argument("--recursion-limit", "-r", type=int, default=100,
                        help="Recursion limit for processing (default: 100)")

    args = parser.parse_args()

    try:
        user_prompt = input("🔨 CodeForge - describe the project you want built: ")
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": args.recursion_limit}
        )
        print("\n✅ CodeForge finished. Final state:", result)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()