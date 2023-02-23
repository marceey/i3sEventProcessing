# i3sEventProcessing
README

This project aims to preprocess an event-based lip reading dataset called 2022_i3s_EventLipReadingDataset for data analysis and experiments with the state-of-the-art MSTP algorithm. The following functions are included in the project:

    quadratic_crop_event(event, newsize): This function crops the input event stream to a quadratic shape with a specified size.

    timestamp_crop(event, first_timestamp, last_timestamp): This function crops the input event stream to contain events that fall within a specified timestamp range.

    scatterplot_event(event): This function generates a scatter plot visualization of the input event stream.

    blackwhite_image(event): This function generates a black and white image from the input event stream.

    face_landmarks(image): This function detects faces in an input image and draws landmarks on each face.

Additionally, the project includes a data processing pipeline (datapipeline.py) to reduce and optionally crop and restructure events of the i3s dataset. The pipeline uses the EventCount function from the reduceEvents module to downsample the event stream. The downscaling factor can be specified with the div parameter.

To use the pipeline, specify the input and output paths and phase, and run the script. The pipeline will load the events and timestamps from the specified input path, reduce the events using EventCount, optionally crop and restructure the event stream, and save the reduced events to the specified output path.
