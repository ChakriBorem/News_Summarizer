### 📰 AI-Powered News Summarizer

---

## 🚀 Objective
To build and deploy an **AI-based News Summarization Web App** that:
- Accepts a news article URL as input.
- Fetches and parses article content automatically.
- Generates a concise summary using Python text processing.
- Runs on **Azure Functions (serverless)** and is connected to a web frontend via **CORS**.

---

## 🧠 Tech Stack
| Component     | Technology Used                                          |
| ------------- | -------------------------------------------------------- |
| Backend       | Azure Functions (Python 3.11)                            |
| Frontend      | HTML, CSS, JavaScript                                    |
| Libraries     | Requests, BeautifulSoup, Newspaper3k                     |
| Cloud Hosting | Microsoft Azure                                          |

---

## ⚙️ Setup Instructions

### 🧩 Backend — Azure Function (Python)

```
1. Create a Resource Group:
az group create --name UploaderRG --location centralindia

2. Create a Storage Account:
az storage account create --name chakrinewsstore --location centralindia --resource-group UploaderRG --sku Standard_LRS

3. Deploy the Azure Function:
func azure functionapp publish chakrinewssummarizer

4. Get the Function Endpoint:
https://chakrinewssummarizer-fbgmcadpepd3aucb.centralindia-01.azurewebsites.net/api/summarizenews

5. Enable CORS for the frontend:
az functionapp cors add --name chakrinewssummarizer --resource-group UploaderRG --allowed-origins "https://chakrinewsfrontend.z29.web.core.windows.net"
```

### 🌐 Frontend — Static Web App

1. Create a simple index.html file for user input and summary display.

2. Upload it to Azure Blob Storage with Static Website Hosting enabled.

3. Configure the endpoint:

4. The frontend sends a POST request to the Function App using JavaScript fetch().

---

## ⚠️ Challenges Faced

| 🧩 Issue | 🔍 Description | 🛠️ Solution |
|-----------|----------------|--------------|
| **Azure Region Restriction** | Faced issues while deploying the Linux-based Azure Function App due to restricted regions in the subscription. | Deployed successfully in the **Central India** region which supports Python-based Azure Functions. |
| **CORS Errors** | Frontend (HTML) couldn’t communicate with the Azure Function API due to CORS policy restrictions. | Added allowed origins using the command:<br>`az functionapp cors add --name chakrinewssummarizer --resource-group UploaderRG --allowed-origins "https://chakrinewsfrontend.z29.web.core.windows.net"` |
| **Article Parsing Failures** | Some URLs (especially older BBC/CNN links) returned 404 or invalid content. | Added **fallback parsing** using `BeautifulSoup` when `Newspaper3k` fails to extract article text. |
| **Version Mismatch** | Local Python version (3.13) caused dependency conflicts during function deployment. | Switched to **Python 3.11** environment for compatibility with Azure Functions runtime. |

---

