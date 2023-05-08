import click
import openai
import inspect

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@click.command()
@click.argument('filename', type=click.Path(exists=True), required=True)
@click.option('--api-key', envvar='OPENAI_API_KEY')
@click.option('--model', default="gpt-3.5-turbo")
@click.option('--temperature', default=0.7)
@click.option('--railings/--no-railings', default=True)
def main(filename, api_key, model, temperature, railings):
    openai.api_key = api_key

    prompt = """
        You take in wrong, incomplete or partial Python 3 code and output a fixed version that is
        syntactically correct and actually does what the user intended. The outputted code
        should not have any sections that still need implementing and should be able to be
        run by a Python interpreter. This means filling in any TODO or "blah blah blah" comment
        with the actual implementation. Don't worry about how the user wants to implement the function,
        just guess. Do not give any explanation or preamble, just the code block. If there is a problem,
        start your response with "error: " and give a VERY SASSY compiler or interpreter. Make your response
        as sassy as possible if there is an error. Keep errors short. You can include snippets of the original
        code in the error but not any new implementation.
    """

    cleaned = " ".join([line.strip() for line in prompt.split("\n")]).strip()

    with open(filename, "r") as f:
        contents = f.read()

        print

    response = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=[
                {"role": "system", "content": cleaned},
                {"role": "user", "content": contents},
            ]
    )

    code = response['choices'][0]['message']['content']

    if code.startswith("error"):
        print(bcolors.FAIL + code + bcolors.ENDC)
        return

    code = code.strip("```").strip("\n")

    if not railings:
        print(bcolors.OKCYAN + "-- Code to run --" + bcolors.ENDC)
        print(bcolors.OKGREEN + code + bcolors.ENDC)
    
    if railings:
        print(bcolors.WARNING + "\n\n-- Continue? --" + bcolors.ENDC)
        response = input("[yes]/no: ")

        if response != "" and response != "yes":
            print(bcolors.FAIL + "\nAborting..." + bcolors.ENDC)
            exit()

    print(bcolors.OKCYAN + "\n\n-- Output --" + bcolors.ENDC)
    exec(code, locals(), locals())