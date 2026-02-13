**LAB 04_ SCREENSHOTS**

<img width="958" height="511" alt="SS3" src="https://github.com/user-attachments/assets/3d583cdc-25fe-4567-a9e3-a583e8582c0e" />
<img width="959" height="511" alt="SS1" src="https://github.com/user-attachments/assets/ea84e33c-873e-441b-8b39-9be36bf75c11" />
<img width="959" height="511" alt="SS2" src="https://github.com/user-attachments/assets/778fe257-04f3-4cf1-a4d4-7f93f3aebdad" />
<img width="958" height="511" alt="SS3" src="https://github.com/user-attachments/assets/6e3bbbc9-6a07-40ae-a5a5-84356543052c" />
<img width="959" height="512" alt="SS4" src="https://github.com/user-attachments/assets/d8aee32b-6c40-439b-93dc-d24b15617145" />

**LAB 04 DATASET DESCRIPTION**

**Overview:**
The dataset is a multimodal collection consisting of text documents and images. It is designed to build a retrieval system where users can pose queries, and the system retrieves relevant textual and visual information.

Text modality: Contains text chunks from various documents (e.g., reports, articles, manuals).

Image modality: Contains images with captions extracted from filenames. These images correspond to topics or entities in the text.

**Structure**

The dataset is stored in the folder:

project_data_mm/
│
├─ doc1.txt
├─ doc2.txt
├─ doc3.txt
│
└─ Images/
    ├─ image1_caption.png
    ├─ diagram_2.jpg
    └─ chart3.jpeg


*.txt → Text files, each representing a document or page.

Images/ → Folder containing image files (PNG, JPG, JPEG).

Captions for images are derived from the filenames (underscores _ replaced with spaces).

**Data Fields**
Text Chunks
Field	Description
chunk_id	Unique ID for the chunk, e.g., doc1.txt::p1
doc_id	Source document filename, e.g., doc1.txt
page_num	Page number (simplified to 1 in this dataset)
text	Cleaned text content of the document

**LAB 04 - REFLECTIONS**

In this lab, I learned how to build a multimodal retrieval system that combines both text and image data. Implementing TF-IDF for text and image captions provided hands-on experience with vectorization, normalization, and similarity search.

The process of cleaning and preprocessing text, indexing the dataset, and then retrieving relevant evidence based on user queries helped me understand the core principles of information retrieval.

I also gained insight into Streamlit UI development, enabling me to quickly create a user-friendly interface for interacting with the retrieval system. This lab strengthened my understanding of data preprocessing, feature extraction, and retrieval pipelines in a practical setting.
