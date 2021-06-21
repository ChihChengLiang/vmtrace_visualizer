import json
from time import sleep
import os


def main():
    with open("./example/example_1.json", "r") as f:
        j = json.load(f)
        size = len(j["structLogs"])

        for step, log in enumerate(j["structLogs"]):
            os.system("clear")
            print("step", step, '/', size)
            print("pc", log["pc"])
            print("gas", log["gas"])
            print("\n[storage]")
            if log["storage"]:
                for k, v in log["storage"].items():
                    print(k, v)
            print("\n[memory]")
            if log["memory"]:
                for mem_i, item in enumerate(log["memory"]):
                    print(mem_i * 32, "\t", int(item, 16))
            print("\n[stack]")
            args = ""
            if log["op"].startswith("PUSH"):
                args = int(j["structLogs"][step + 1]["stack"][-1], 16)
            print("*", log["op"], args, "*******", log["gasCost"])
            if log["stack"]:
                for stack_i, item in enumerate(reversed(log["stack"])):
                    print(stack_i, "\t", int(item, 16))

            sleep(0.5)


if __name__ == "__main__":
    main()
