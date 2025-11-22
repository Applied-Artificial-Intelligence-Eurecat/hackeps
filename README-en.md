<p align="right"><a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README.md">Català</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-es.md">Español</a> | <a href="https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/blob/main/README-en.md">English</a></p>

-----

<h1 align="center">

💫  NebulOuS: Your own Multi-Cloud-edge Cluster ☁️

</h1>

-----

- [Challenge 🔎](#the-challenge-)
  - [Objectives](#objectives)
  - [What We Provide](#what-we-provide)
  - [Considerations](#considerations)
- [Documentation and Information](#documentation-and-information)
  - [Clusters](#clusters)
  - [Google Cloud](#GCP)
  - [Amazon](#AWS)
- [Winners 🏅](#winners-)
  - [Evaluation](#evaluation)
  - [The Prize 🤑](#the-prize-)

-----

# The challenge 🔎

Google Cloud, Amazon Web Services, Microsoft Azure... big providers that may eventually fail, and they do (some more than others 😶‍🌫️). And in that moment, everyone wishes they didn't depend on just one. 
That's why this year we propose helping that poor soul who made the mistake of trusting only one of them, and create a platform to deploy clusters of machines across different providers 🤙 Software Development, AI, DevOps... in this challenge you'll be able to practice all kinds of disciplines to reach your goal 😎
And let's think locally: who doesn't have at home a server with 8 CPUs and 16 GB of RAM waiting to be used to deploy things?


## Objectives

The final objective is easy to say: **a platform to create multi-cloud-edge clusters**, but achieving it can be a bit more overwhelming.

For this reason, we suggest some functional points, and as we say every year: **NO**, you don't need to do all of them (it's a hackathon), and you are free to give your platform your own original approach — we only suggest ideas ;) And if you want to follow the ideas, you don't need to do them in this order either... If something doesn't work out, try moving on to the next one.

And if not... just ask us!
<h4 align="center">

![](https://camo.githubusercontent.com/abee1b0ea2fb94ffd75986431a093a0f22aeb534a70d11b3fa493f2eda877355/68747470733a2f2f6d656469612e74656e6f722e636f6d2f616556383058443443536741414141642f677569646c696e65732d706972617465732d6f662d7468652d63617269626265616e2e676966)

_The Code is more what you'd call "guidelines" than actual rules._
</h4>

### Device Management
**000 - Hello? It's me!**

Connect to the GCP and AWS APIs using the credentials we'll provide, and even allow multiple registered accounts.

**001 - Cloud? It's just someone else's computer!**

Besides the cloud, it's also interesting to have _edge_ devices, such as your own computer (or a VM), Raspberry Pis, etc. Having a list of these devices and being able to register and deregister them can also be useful.
Register and deregister Edge nodes 
> If you want to connect via SSH to Raspberry Pis or colleagues' computers, apart from being careful with firewalls, use mobile network, as Eduroam tends to have the bad habit of blocking these types of connections.

**010 - What's in the cloud?**

Being able to see which nodes can be created in cloud providers: machine types, resources, costs, etc. Additionally, it's interesting to be able to filter or search for machine types that meet certain HW and CPU requirements.

### Cluster Creation

**011 - The cluster must be created**

Given a need for X machines with Y resources per machine, you'll need to choose which cloud provider and which instances to deploy, or which edge devices to use.

> It's totally valid to allow the user to manually choose which instances to use, although you can also try to choose "automatically" based on metrics you consider (price? ping? location?)

**100 - LIAR! This is not a cluster**

Once the _edge_ nodes are chosen and/or the cloud machines are created, the necessary software should be installed and configured (automatically) on them so they act as a cluster.

> Some options, from less to more complex, are Nomad, Docker Swarm, K3s or Kubernetes (but you can use whatever you want, even if you want to develop something of your own)

### Monitoring and Deployment

**101 - Everything is going great, very well, okay... bad!**

Allow the user to review the status of the cluster(s) and the resource consumption of the nodes.

**110 - What's this good for?**

Allow the user to deploy an application on the cluster.

## What do we give you? 
Teams interested in participating will receive:
- A Service Account to create and manage machines in `Google Cloud` (Compute Engine)
- An API Key to create and manage machines in `Amazon Web Services` (EC2)
- Access to an LLM API so you can generate and process natural language 

## Considerations
It is strictly forbidden to share the key assigned to you with other groups.

Please create all machines in European regions.

For security reasons, creating VMs with associated graphics is not allowed.

To avoid problems, in Google Cloud Platform, external connections from any IP to all ports of the machines you create are allowed.


### VERY, VERY, VERY IMPORTANT
Please make sure to EXCLUDE credentials from the public GitHub repository. You can create a `.gitignore` file in your project root and add:
```.gitignore
**.json
```
Every important warning has a story behind it

![](https://i.imgflip.com/aaq9wn.jpg)
---
# Documentation and Information
You can connect to a machine via [**SSH**](https://www.cloudflare.com/es-es/learning/access-management/what-is-ssh/). Besides connecting via "username and password", you can also register an SSH key that you can generate with:

```sh
ssh-keygen -t rsa -b 4096 -C "username"
```

This gives you a private key (with the name you specify) and a public one (the name you specify + `.pub`). When creating a machine in both AWS and GCP, you can provide the public key so you can connect via SSH later:
```sh
ssh -i <file> username@MACHINE-IP
```

## Clusters
```arduino
[AWS]          [Azure]          [GCP]
 Client VM     Client VM       Client VM
      \           |              /
       \          |             /
        \         |            /
            Master Node (VM)
```
- [Docker Swarm](https://docs.docker.com/engine/swarm/)
- [Nomad](https://developer.hashicorp.com/nomad)
- [K3s](https://k3s.io/)
- [K8s (Kubernetes)](https://kubernetes.io/)


## GCP
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" width="300"/>

In Google Cloud Platform you can use the command line, and you'll need to install and configure [`gcloud`](https://docs.cloud.google.com/sdk/docs/install).
You also have specific libraries for almost every programming language:
- [Go](https://docs.cloud.google.com/go/docs)
- [JavaScript](https://docs.cloud.google.com/nodejs/docs)
- [Python](https://docs.cloud.google.com/python/docs)
- [Java](https://docs.cloud.google.com/java/docs)
- [C++](https://docs.cloud.google.com/cpp/docs)
- [C#](https://docs.cloud.google.com/dotnet/docs)

You have examples of how to use the libraries at [Google Cloud Platform's Github account](https://github.com/GoogleCloudPlatform).
Specifically, the _product_ used is [Compute Engine](https://cloud.google.com/products/compute?hl=es)

It is recommended to set the documentation language to English, as the Spanish versions are quite deficient.

Additionally, you have some ChatGPT-made examples so you can test without going crazy in this same repository, at `examples\google-cloud-platform`. Check the README associated with the language you want to try.

- [Python](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/python)
- [Java](https://github.com/Applied-Artificial-Intelligence-Eurecat/hackeps/tree/main/examples/google-cloud-platform/java)

## AWS
<img src="https://miro.medium.com/v2/resize:fit:1200/1*neG4D9C8UcJvNn6bverfIA.png" width="300"/>

---
# Winners 🏅
This time, two winning teams will be selected:
- **Winners:** A prize for the team that achieves the most balanced solution between quality, execution, and idea
- **Rising Stars:** A prize for teams whose members have no prior knowledge, who present a well-designed solution and demonstrate learning ability.

### What will be evaluated? 
Both the demo presented during the final presentation and all the information included in the Devpost submission will be evaluated (remember that you can update it even after the deadline). Based on this, we will evaluate, **mainly**:

**For the first prize**
- **Implemented ideas:** The level of originality will be taken into account, proposals that go beyond the basics, the proposed flows, and any novel functionality that is useful or practical.

- **Functionality:** How well the project works as a whole, the state of each part, and the quality of integration between them.

- **Architecture:** We will assess whether the proposed architecture would make sense in a real environment, if it is scalable, and if it is well designed.

- **Technologies:** It's not about the language itself, but the complementary technologies used: web frameworks (React, Angular, Vue…), databases (Mongo, Postgres, MariaDB…), containers (Docker), etc.

- **Code quality:** Even though it's a hackathon, we will consider avoiding excessive hardcoding, maintaining minimum good practices (indentation, typing in non-strictly typed languages, project organization…).

**For Rising Stars**
- **Implemented ideas:** Same as in the general category, originality and the contribution of useful functionalities beyond the basics will be valued.

- **Learning:** Whether there was prior experience or not, what you learned in these 24 hours, the main challenges encountered and how you solved them.

- **Teamwork:** How you organized yourselves, task distribution, and collaboration dynamics.

- **Code quality:** Same criteria as in the main category: avoid unnecessary hardcoding and maintain a minimum of order and coherence.

- **Idea presentation:** Clarity in explaining the proposal, its approach, and its objective.


## The prize 🤑

- Amazon voucher worth €1000 for the **first prize**
- Amazon voucher worth €200 for the **Rising Stars** prize
