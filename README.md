<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:07090e,50:0086FF,100:00AEC7&height=210&section=header&text=Abraão%20Teixeira&fontSize=42&fontColor=ffffff&animation=fadeIn&desc=Cloud%20Native%20Security%20%7C%20eBPF%20%7C%20Kubernetes&descSize=18&descAlignY=70&descAlign=50" width="100%" alt="Abraão Teixeira - Cloud Native Security | eBPF | Kubernetes" />
</div>

<br/>

<div align="center">
  <p>
    <a href="https://www.cncf.io/"><img src="https://img.shields.io/badge/CNCF-Landscape%20Specialist-0086FF?style=for-the-badge&logo=cncf&logoColor=white" /></a>
    <a href="https://kubernetes.io/"><img src="https://img.shields.io/badge/Kubernetes-Production%20K8s-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" /></a>
    <a href="https://falco.org/"><img src="https://img.shields.io/badge/Falco-eBPF%20Runtime%20Sec-00AEC7?style=for-the-badge&logo=falco&logoColor=white" /></a>
    <a href="https://cilium.io/"><img src="https://img.shields.io/badge/Cilium-eBPF%20Networking-F5A623?style=for-the-badge&logo=cilium&logoColor=white" /></a>
    <a href="https://www.fortinet.com/"><img src="https://img.shields.io/badge/Fortinet-Zero%20Trust%20Sec-EE3124?style=for-the-badge&logo=fortinet&logoColor=white" /></a>
    <a href="https://www.vmware.com/"><img src="https://img.shields.io/badge/VMware-vSphere%20%7C%20NSX-0095D3?style=for-the-badge&logo=vmware&logoColor=white" /></a>
    <a href="https://www.linux.org/"><img src="https://img.shields.io/badge/Linux-Kernel%20%26%20Systems-FCC624?style=for-the-badge&logo=linux&logoColor=black" /></a>
  </p>
</div>

---

```yaml
# ── OPERATIONAL TELEMETRY ───────────────────────────────────────────
engineer:
  name: "Abraão Teixeira da Silva"
  location: "Brusque, SC - Brazil"
  education: "Computer Networks @ Instituto Federal Catarinense (IFC)"
  role: "Cloud Native & Infrastructure Security Specialist"
  focus_domains:
    - "eBPF Runtime Security & Kernel Tracing (Falco / Cilium)"
    - "Kubernetes Cluster Architecture & Multi-Tenant Hardening"
    - "Enterprise Virtualization & Hybrid Cloud (VMware vSphere 8 / NSX)"
    - "Next-Gen Network Security & Zero Trust Perimeter (Fortinet)"
    - "Linux Kernel Tuning & High-Throughput Packet Processing"
  mantra: "In eBPF and Kernel We Trust, All Others Must Bring Zero Trust Proof."
```

---

## ⚡ Core Engineering Pillars

<table>
<tr>
<td width="50%" valign="top">

### ☁️ Cloud Native & Kubernetes (CNCF)
* **Orquestração:** Kubernetes (Bare-Metal & Cloud), VMware Tanzu (TKG), K3s
* **eBPF & Networking:** Cilium CNI, Hubble Observability, XDP, eBPF Service Mesh
* **Observabilidade:** Prometheus, Grafana, OpenTelemetry, CoreDNS
* **Delivery & IaC:** Helm Charts, Kustomize, Terraform, Ansible

</td>
<td width="50%" valign="top">

### 🛡️ Cybersecurity & Runtime Defense
* **Runtime Security:** Falco (Modern eBPF driver, syscall filtering, custom rulesets)
* **Perímetro & Zero Trust:** Fortinet FortiGate, FortiManager, SD-WAN, IPS/IDS
* **Hardening & Auditoria:** CIS Benchmarks, NIST 800-53, Linux Kernel Hardening
* **Container Security:** Trivy Vulnerability Scanner, OPA Gatekeeper, Cosign

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🖥️ Enterprise Virtualization (VMware)
* **Hypervisor & Core:** VMware vSphere 7/8, ESXi, vCenter Server
* **Software-Defined Network:** VMware NSX-T (Microsegmentação, Overlay)
* **Storage & Resiliência:** vSAN, High Availability (HA), DRS, Fault Tolerance
* **Híbrido:** Integração vSphere + Kubernetes Container Runtime

</td>
<td width="50%" valign="top">

### 🐧 Linux Systems & Kernel Engineering
* **Sistemas:** Debian, Ubuntu Server, Rocky Linux, Red Hat Enterprise Linux (RHEL)
* **Kernel & Tuning:** `sysctl` TCP/IP stack tuning, `cgroups v2`, namespaces, TC/BPF
* **Linguagens & Scripts:** Go (Golang), Python, Bash/Shell Script, C/C++, PowerShell
* **Análise de Redes:** Protocolos TCP/IP, Wireshark, BGP, OSPF, VLANs

</td>
</tr>
</table>

---

## 🧭 CNCF & Enterprise Landscape Mastered

```
+-------------------------------------------------------------------------------+
|                        CLOUD NATIVE & CYBER LANDSCAPE                         |
+-------------------------------------------------------------------------------+
| PROVISIONING  | Terraform · Ansible · Helm · Containerd                       |
| RUNTIME       | Kubernetes · Cilium (eBPF) · CRI-O · containerd               |
| SECURITY      | Falco (Graduated) · Fortinet Zero Trust · Trivy · OPA         |
| NETWORKING    | Cilium Hubble · Envoy Proxy · MetalLB · FortiGate SD-WAN      |
| OBSERVABILITY | Prometheus · Grafana · OpenTelemetry · Zabbix                 |
| HYBRID CLOUD  | VMware vSphere · ESXi 8.0 · NSX-T · Tanzu Kubernetes Grid     |
+-------------------------------------------------------------------------------+
```

---

## 📊 Live Terminal Monitor

```console
abraao@sec-ops-node01:~$ cilium status --verbose
    /¯¯\
 /¯¯\__/¯¯\    Cilium:             OK
 \__/¯¯\__/    Operator:           OK
 /¯¯\__/¯¯\    Hubble Relay:       OK
 \__/¯¯\__/    ClusterMesh:        OK
    \__/

Deployment        cilium-operator            Desired: 2, Ready: 2/2, Available: 2/2
DaemonSet         cilium                     Desired: 6, Ready: 6/6, Available: 6/6
Containers:       cilium-agent               Running: 6
                  ebpf-runtime-security      Enabled (Falco engine v0.39.0 hooked)
Perimeter Status: FortiGate Active-Active HA · Zero-Trust Tagging Synced
Hypervisor:       VMware ESXi 8.0 Cluster    · DRS 100% Balanced · vSAN Healthy
Kernel Security:  eBPF JIT Active            · cgroups v2 Loaded · Syscall Audit OK
```

---

## 📈 GitHub Telemetry & Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=abraaoteixeira&show_icons=true&theme=tokyonight&hide_border=true&bg_color=07090e&title_color=0086FF&icon_color=00AEC7&text_color=c0cde8" height="155" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=abraaoteixeira&layout=compact&theme=tokyonight&hide_border=true&bg_color=07090e&title_color=0086FF&text_color=c0cde8" height="155" alt="Top Languages" />
</div>

<div align="center">
  <img width="100%" src="https://streak-stats.demolab.com/?user=abraaoteixeira&theme=tokyonight&hide_border=true&background=07090e&ring=0086FF&fire=00AEC7&currStreakNum=c0cde8&sideNums=c0cde8&currStreakLabel=0086FF&card_width=850" alt="GitHub Streak" />
</div>

---

<div align="center">
  <h3>📬 Conecte-se comigo:</h3>
  <a href="https://www.linkedin.com/in/abraaoteixeira/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:abraaoteixeira0101@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/abraaoteixeira"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</div>

<br/>

<p align="center">
  <sub>⚡ Constantly architecting the future of secure, resilient and high-throughput cloud platforms.</sub>
</p>