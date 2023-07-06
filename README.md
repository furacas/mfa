# MFA 客户端

该项目是一个多因素身份验证（MFA）客户端。此应用允许用户录入多个账户的 MFA 密钥，以在一个界面上显示所有账户的 MFA 计算结果。

市面上的MFA客户端很多，但是很少有Web客户端，因为某些原因要和一群人（内网环境）共享MFA，但是密钥不太方便共享出去，需要统一管理，于是就自己写一个客户端。


## 安装步骤

### docker
```bash
docker run -d -p 8501:8501 -v /path/to/your/data:/data furacas/mfa
```


### python

**克隆仓库**
```bash
git clone https://github.com/furacas/mfa.git
cd mfa
```
**安装依赖**
```bash
pip install -r requirements.txt
```
**运行**
```bash
streamlit run MFA_Client.py
```

# MFA Client
This project is a multi-factor authentication (MFA) client. The application allows users to enter the MFA keys of multiple accounts and displays the MFA calculation results of all accounts on a single interface.

While there are numerous MFA clients available, web-based clients are quite rare. In certain scenarios, it may be necessary to share MFA information with a group of people (within an intranet environment), but sharing the keys might not be convenient and requires centralized management. For this reason, we've decided to develop our own client.

## Installation Steps
### Docker
```
docker run -d -p 8501:8501 -v /path/to/your/data:/data furacas/mfa
```

### Python
**Clone the repository**
```bash
git clone https://github.com/furacas/mfa.git
cd mfa
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Run the application**
```bash
streamlit run MFA_Client.py
```
