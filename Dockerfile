FROM nvcr.io/nvidia/pytorch:23.08-py3

WORKDIR /code

RUN apt-get update && rm -rf /var/lib/apt/lists/*

RUN pip install --extra-index-url https://pypi.nvidia.com nemo-curator[cuda12x]
RUN pip install jupyter lxml_html_clean

CMD ["bash"]