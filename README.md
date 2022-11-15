# DNS-practice
HHA 504 / Cloud Computing / Assignment 8 / Domain Names


## This repo aims to:
- Utilize my flask app from [flask-with-db](https://github.com/alicewu1/flask-with-db) repo and deploy via GCP VM
- Create an A record that links together my domain with the IP address of my flask app deployed on GCP



# Register a domain name using .TECH
- Using [get.tech](https://get.tech/github-student-developer-pack) 
- Domain Name: **alice-wu.tech**

# Create a A record that links together the domain with the IP address of your flask app deployed on either GCP or Azure 
- Under your get.tech Control Panel, navigate to **Manage Orders > List/Search Orders**
- Select your new domain name and scroll down to **DNS Management**
- Select **Manage DNS**
- Under **(A) Records** > **Add a Record**
    -       Host Name: @
            Destination IP Address: [GCP VM External IP Address]
            TTL: 7200


# Set Up GCP VM 
- by following instructions from **setup.GCP.md** 
- Verify flask is deployed by refreshing your domain name in your browser


# **images** folder
- contains screenshots of my live flask app deployed on my website