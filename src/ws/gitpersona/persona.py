import argparse
import re
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Specify or list repository-local persona(s).')
    parser.add_argument('--name', '-n', help='persona name')
    options = parser.parse_args(argv)
    personas = list_personas()
    if options.name:
        persona = personas.get(options.name)
        if not persona:
            print('Persona "{}" not found'.format(options.name))
            raise SystemExit(1)
        print('Setting user.name="{name}", user.email="{email}"'.format(
            **persona))
        set_persona(persona)
    else:
        print('Known personas:')
        for name, persona in personas.items():
            print('  {persona} {name} <{email}>'.format(
                persona=name.ljust(12), **persona))
        print('Current username:')
        print('  {name} <{email}>'.format(
            name=cmd('git config user.name'),
            email=cmd('git config user.email')))


CONFIG_PERSONA = re.compile('^persona\\.(.*?) ([^<]*) <(.*?)>$')


def list_personas():
    result = {}
    config = cmd('git config --global --get-regex ^persona\\.')
    for line in config.splitlines():
        match = CONFIG_PERSONA.search(line)
        if not match:
            continue
        result[match.group(1)] = {
            'name': match.group(2), 'email': match.group(3)}
    return result


def set_persona(persona):
    cmd('git config --local user.name "{}"'.format(persona['name']))
    cmd('git config --local user.email "{}"'.format(persona['email']))


def cmd(cmd):
    process = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # XXX This simply assumes utf8 -- is that feasible?
    return stdout.strip().decode('utf8')
