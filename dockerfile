FROM python
RUN pip install flask
RUN mkdir /app
COPY dhanno.py /app/
EXPOSE 7000
CMD [ "python","/app/dhanno.py" ]
