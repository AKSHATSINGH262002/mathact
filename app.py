import streamlit as st
from PIL import Image
import os 
import cv2
from pytesseract import pytesseract 
import  matplotlib.pyplot as plt
import numpy as np
import pre
flag=0
img=Image.open('MATHION.png')
st.set_page_config(page_title="MATH-ACTION",page_icon=img)
st.header("--MATH-ACTION--")

uploaded_file=st.file_uploader("choose file",type=["jpeg","png","jfif","jpg"])
if uploaded_file is not None:
        image=Image.open(uploaded_file)
        st.image(image)
        text=pre.extract(image)
        #arr=text.split()
        extracted_text=pre.extract(image)
            
            # Display the extracted text
        st.write("Extracted Text:")
        st.text(extracted_text)
        #print(arr)
        if st.button("DETECT"):
            for i in text:
    
                x=np.linspace(0,2*np.pi,100)
                n=np.linspace(-2 * np.pi, 2 * np.pi, 1000)
                s=np.linspace(0.1, 10, 1000)
                t=np.linspace(-2, 2, 1000)
                if(i=="sin" or i=="Sin"or i=="sin(x)" or i=="sine" or i=="sinx"):

                    y_sin=np.sin(x)
                    fig,ax=plt.subplots()
                    ax.plot(x,y_sin,label='sin x',color='red',linewidth=2)
                    plt.xlabel('x')
                    plt.title('sin x graph')
                    st.pyplot(fig)
                    #break
               

                elif(i=="cos"or i=="Cos" or i=="cos(x)" or i=="cosine"or i=="cosx"):

                    y_cos=np.cos(x)
                    fig,ax=plt.subplots()
                    ax.plot(x,y_cos,label='cos x',color='red',linewidth=2)
                    plt.xlabel('x')
                    plt.title('cos x graph')
                    st.pyplot(fig)
                    #break
                

    
                elif(i=="tan"or i=="Tan" or i=="tan(x)" or i=="tangent"or i=="tanx"):
                
                    y_tan=np.tan(n)
                    fig,ax=plt.subplots()
                    ax.plot(n,y_tan,label='tan(x)',color='blue')
                    plt.xlabel('x')
                    plt.ylabel('tan(x)')
                    plt.title('tan(x) graph')
                    plt.ylim(-10,10)
                    ax.grid(True)
                    ax.legend()
                    st.pyplot(fig)
                    #break
    
                elif(i=="cosec"or i=="Cosec" or i=="cosec(x)"):

                    y_cosec=1/np.sin(n)
                    fig,ax=plt.subplots()
                    ax.plot(n,y_cosec,label='cosec(x)',color='green',linewidth=2)
                    plt.xlabel('x')
                    plt.ylabel('cosex(x)')
                    plt.title('cosec(x) graph')
                    plt.ylim(-10,10)
                    st.pyplot(fig)
                    #break

            
                elif(i=="sec"or i=="Sec" or i=="sec(x)"):

                    y_sec=1/np.cos(n)
                    fig,ax=plt.subplots()
                    ax.plot(n,y_sec,label='sec(x)',color='green',linewidth=2)
                    st.pyplot(fig)
                    #break
            
                elif(i=="log"):
                

                    y=np.log(s)
                    fig,ax=plt.subplots()
                    ax.plot(s,y,label='log(x)',color='orange')
                    st.pyplot(fig)

                    #break
                elif(i=="e^x"):
                    y_exp=np.exp(t)
                    fig,ax=plt.subplots()
                    ax.plot(t,y_exp,label='exponential',color='orange')
                    ax.title('exponential')
                    ax.xlabel('x')
                    ax.ylabel('exponential')
                    st.pyplot(fig)


                else:
                    flag=1
        if(flag==1):
            print("no more function found")




      


    
    
    








