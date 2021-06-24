# A-tool-for-Automatic-generation-and-annotation-of-a-French-traffic-signs-dataset-for-deep-learning

## Abstract
Vision based traffic sign detection plays a vital role in intelligent transportation systems. Recently, many deep learning­based traffic sign detection methods have been proposed, and compared to traditional methods, they show better performance. However, due to the difficult conditions of the driving environment and the size of the traffic signs in the traffic scene images, the performance of the deep learning based method in detecting small traffic signs remains limited. Furthermore, the inference speed of state of the art traffic sign detection methods is still very slow. Also models have to be trained on good labeled datasets in order to get good results. But collecting and annotating dataset takes too much time and done manually by people. This paper proposes two approaches to make this process faster by making it automated. First aproach is to detect traffic signs using pretrained models(transfer learning) trained on The German Traffic Sign Recognition Bench mark(GTSRB) dataset which anotated manually. And the second one is to use Haar Cascades Classifier. After detecting traffic signs, they annotated automatically with region of interest, height, width and other labels.

For more information you can read `A_tool_for_Automatic_generation_and_annotation_of_a_French_traffic_signs_dataset_for_deeplearning.pdf` file.

## How to run

`python3 main.py`

`python3 write_csv.py`
