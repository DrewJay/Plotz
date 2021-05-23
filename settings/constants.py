# Folder generation settings.
WRAPPER_FOLDER_NAME = "vae"
RUN_ID = "1"
RESULTS_FOLDER_NAME = "output"
RUN_FOLDER_NAME = ("run/%s/" % WRAPPER_FOLDER_NAME) + "_".join([RUN_ID, RESULTS_FOLDER_NAME])
MODE = "build"
DATA_FOLDER_NAME = "./data/train/"
IMAGE_FOLDER = "./data/train/images/"
NETWORK_VISUALIZATION_FOLDER_NAME = "architecture"
WEIGHTS_FOLDER_NAME = "weights"
SAMPLE_RESULTS_FOLDER_NAME = "generatedSamples"
CSV_NAME = "list_attr_celeb.csv"

# Training metadata.
INPUT_DIM = (128, 128, 3)
Z_DIM = 350
BATCH_SIZE = 32
LEARNING_RATE = 0.001
RECONSTRUCTION_LOSS_FACTOR = 10000
EPOCHS = 300
PRINT_EVERY_N_BATCHES = 100
INITIAL_EPOCH = 0

# Analysis metadata.
ANALYSIS_BATCH_SIZE = 500
