from codecarbon import EmissionsTracker
import llm

tracker = EmissionsTracker()

tracker.start()
try:
    # Compute intensive code goes here
    model = llm.get_model("orca-mini-3b-gguf2-q4_0")
    response = model.prompt(
        "What food should I eat if I am visiting Vigo for the first time?"
    )
    print(response.text())
finally:
    tracker.stop()
