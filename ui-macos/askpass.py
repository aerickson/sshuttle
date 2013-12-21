import sys, os, re, subprocess

def askpass(prompt):
    prompt = prompt.replace('"', "'")

    if 'yes/no' in prompt:
        return "yes"

    script="""
        tell application "Finder"
            activate
            display dialog "%s" \
              with title "Sshuttle SSH Connection" \
              default answer "" \
              with icon caution \
              with hidden answer
        end tell
    """ % prompt

    p = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE)
    out = p.stdout.read()
    rv = p.wait()
    if rv:
        return None
      # 10.8 code
#    g = re.match("text returned:(.*), button returned:.*", out)
# 10.9 code
    g = re.match("button returned:.*, text returned:(.*)", out)
    if not g:
        return None
    return g.group(1)
