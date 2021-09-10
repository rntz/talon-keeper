from talon import actions, speech_system

def hook(d):
    try: words = d["parsed"]._unmapped
    except KeyError: return
    if words[0] == "keeper" and actions.speech.enabled():
        actions.auto_insert(' '.join(words[1:]))
        d['parsed']._sequence = []

speech_system.register("pre:phrase", hook)
