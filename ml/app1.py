import streamlit as st

st.title('이미지 분류')
file = st.file_uploader('이미지를 올려주세요', type=['jpg', 'png', 'gif'])

def predict_image(file):
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    
    import cv2
    import tensorflow as tf

    resnet50 = tf.keras.applications.resnet.ResNet50(weights='imagenet', input_shape=(224,224,3))
    from tensorflow.keras.applications.imagenet_utils import decode_predictions

    image = np.array(Image.open(file))
    st.image(image, use_column_width=True)

    image_resized = cv2.resize(image, (224, 224))
    image_reshaped = image_resized.reshape([1, 224, 224, 3])
    predicted = resnet50.predict(image_reshaped)

    decoded_predict = decode_predictions(predicted, top=5)[0]  # 상위 5개 예측 결과를 가져옵니다.
    return decoded_predict

if file is None:
    st.text('이미지를 먼저 선택하세요.')
else:
    with st.spinner('예측 중...'):
        predicted = predict_image(file)
        for i, pre in enumerate(predicted):
            st.success('{}위: {} ({:.2f}%)'.format(i+1, pre[1], pre[2]*100))
