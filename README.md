<div align="center">
  <a href="https://github.com/abraaoteixeira">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=0:07090e,50:0086FF,100:00AEC7&height=210&section=header&text=Abraão%20Teixeira&fontSize=42&fontColor=ffffff&animation=fadeIn&desc=Cloud%20Network%20Engineering%20%7C%20Linux%20Kernel%20%7C%20eBPF%20%7C%20Kubernetes&descSize=16&descAlignY=70&descAlign=50" width="100%" alt="Abraão Teixeira - Cloud Network Engineering | Linux Kernel | eBPF | Kubernetes" />
  </a>
</div>

<br/>

<div align="center">
  <h1>Abraão Teixeira da Silva</h1>
  <h3><code>Network & Cloud Infrastructure Engineer · IFC</code></h3>
  <p>
    <a href="https://www.linuxfoundation.org/"><img src="https://img.shields.io/badge/Linux%20Foundation-LiFT%20Scholar%20'26-brightgreen?style=flat-square&logo=linuxfoundation&logoColor=white" /></a>
    <a href="https://www.cisco.com/"><img src="https://img.shields.io/badge/Cisco-Routing%20%26%20Switching-1BA0D7?style=flat-square&logo=cisco&logoColor=white" /></a>
    <a href="https://www.fortinet.com/"><img src="https://img.shields.io/badge/Fortinet-FortiGate%20%7C%20SD--WAN-EE3124?style=flat-square&logo=fortinet&logoColor=white" /></a>
    <a href="https://ebpf.io/"><img src="https://img.shields.io/badge/Kernel-eBPF%20%2F%20XDP-F5A623?style=flat-square&logo=linux&logoColor=white" /></a>
    <a href="https://kubernetes.io/"><img src="https://img.shields.io/badge/Kubernetes-CKA%20Track-326CE5?style=flat-square&logo=kubernetes&logoColor=white" /></a>
    <a href="https://cilium.io/"><img src="https://img.shields.io/badge/Cilium-eBPF%20CNI-00AEC7?style=flat-square&logo=cilium&logoColor=white" /></a>
    <a href="https://www.vmware.com/"><img src="https://img.shields.io/badge/VMware-vSphere%208%20%7C%20ESXi-0095D3?style=flat-square&logo=vmware&logoColor=white" /></a>
  </p>
</div>

---

```yaml
# ── OPERATIONAL TELEMETRY & PROFILE ─────────────────────────────────
engineer:
  name: "Abraão Teixeira da Silva"
  location: "Brusque, SC - Brazil"
  education: "Computer Networks @ Instituto Federal Catarinense (IFC)"
  role: "Network & Cloud Infrastructure Analyst / Engineer"
  certifications_track:
    - "Linux Foundation LiFT Scholar (Networking Innovator)"
    - "Certified Kubernetes Administrator (CKA)"
    - "Fortinet Certified Professional (FCP Network Security)"
    - "Cisco Network Defense & Routing Fundamentals"
  focus_domains:
    - "Enterprise & Datacenter Networking (L2/L3, OSPF, BGP, VLANs, LACP)"
    - "Next-Gen Firewall, VPNs & Zero Trust Architecture (FortiGate / WireGuard)"
    - "Kernel-Level Dataplane & Packet Processing (eBPF / XDP Hooks)"
    - "Cloud-Native Infrastructure & CNI Networking (Kubernetes / Cilium Hubble)"
    - "Virtualization Platforms & Storage (VMware ESXi 8.0, Proxmox VE, TrueNAS)"
    - "Network Observability & Performance Monitoring (Zabbix, Grafana, Prometheus)"
  mantra: "Packets never lie — from physical layer to kernel space."
```

---

## ⚡ Network & Kernel Datapath

```
  [ Physical NIC / 10GbE ]
             │
             ▼
  ┌───────────────────────────────────────────────────────────┐
  │  DRIVER / XDP HOOK (Kernel Space)                         │
  │  ├── eBPF Bytecode Execution (< 15ns)                     │
  │  ├── 5-Tuple LRU Flow Maps (SYN/ACK/FIN Counters)         │
  │  └── Fast Path Mitigation: XDP_DROP / XDP_PASS            │
  └────────────────────────────┬──────────────────────────────┘
                               │ (Forwarded Packets)
                               ▼
  ┌───────────────────────────────────────────────────────────┐
  │  TC & CNI LAYER (Cilium / eBPF)                           │
  │  ├── BPF Routing & Endpoint Management (Hubble Flow)      │
  │  └── Runtime Audit & System Call Tracing (Falco Engine)   │
  └────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
  ┌───────────────────────────────────────────────────────────┐
  │  USER-SPACE CONTROL PLANE & DAEMONS                       │
  │  ├── ZeroMQ / Unix Sockets Ring Buffer                    │
  │  ├── Topological Threat Inference (STGNN - PyG)           │
  │  └── Hybrid Cloud Virtualization (VMware ESXi 8.0 / NSX)  │
  └───────────────────────────────────────────────────────────┘
```

---

## 🧭 Engineering & Infrastructure Matrix

```
+───────────────────┬──────────────────────────────────────────────────────────+
| DOMAIN            | TECHNOLOGIES & TOOLS                                     |
+───────────────────┼──────────────────────────────────────────────────────────+
| Core Networking   | L2/L3 Switching · OSPFv2 · BGP · VLANs (802.1Q) · LACP   |
| Perimeter Sec     | Fortinet FortiGate · SD-WAN · WireGuard · Zero Trust Tag |
| Kernel Dataplane  | eBPF / XDP Hooks · TC Subsystem · Syscall Tracing        |
| Cloud Native      | Kubernetes · Cilium CNI · Containerd · Helm · MetalLB    |
| Virtualization    | VMware vSphere 8.0 · ESXi · Proxmox VE · TrueNAS Core    |
| Telemetry & NOC   | Zabbix · Grafana · Prometheus · Hubble Service Mesh      |
| Systems & Code    | C++17 · Python (AsyncIO) · Bash Scripting · C (libbpf)   |
+───────────────────┴──────────────────────────────────────────────────────────+
```

---

## 🔬 Research & Projects: SPECTRE_GRID

```
+──────────────────────────────────────────────────────────────────────────────+
| SPECTRE_GRID: Hybrid eBPF/XDP & STGNN Network Intrusion Detection Engine     |
+──────────────────────────────────────────────────────────────────────────────+
| • In-kernel packet filtering with XDP_DROP at sub-microsecond latency.       |
| • Real-time flow state aggregation using eBPF LRU hash tables.               |
| • Space-Temporal Graph Neural Network (STGNN) for lateral movement analysis. |
| • Live distributed deployment across GCP edge honeypots and WSL2 control.    |
+──────────────────────────────────────────────────────────────────────────────+
```

---

## 📊 Active Datapath & Interface Telemetry

```console
abraao@edge-gw01:~$ bpftool prog show name spectre_xdp
128: xdp  name spectre_xdp  tag 4b79a8d9a6c5b0e1  gpl
	loaded_at 2026-09-01T06:00:00-0300  uid 0
	xlated 512B  jited 320B  memlock 4096B  map_ids 42,43

abraao@edge-gw01:~$ ip route show proto ospf
10.100.0.0/16 via 10.0.0.2 dev eth0 metric 20 
10.200.0.0/16 via 10.0.0.3 dev eth0 metric 20 
```

---

## 🏆 Credentials & Verification

| Certification / Grant | Organization | Domain | Year |
| --- | --- | --- | --- |
| **LiFT Scholarship (Networking Innovator)** | Linux Foundation | CKA / Kubernetes & DevOps | 2026 |
| **FortiGate Administrator (FCP Track)** | Fortinet / Adistec | Network Security & SD-WAN | 2026 |
| **Network Defense & Security** | Cisco Networking Academy | Network Defense & Protocols | 2025 |
| **Linux Administration** | 4Linux | Linux Kernel, Daemons & CLI | 2022 |
| **Associate Ethical Hacker** | IBSEC | Threat Assessment & Hardening | 2022 |
| **Google IT Support Professional** | Google | Infrastructure Fundamentals | 2024 |

---

## 📈 Telemetry & Activity

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
  <a href="https://www.linkedin.com/in/abraaoteixeira/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:abraaoteixeira0101@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/abraaoteixeira"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" /></a>
</div>

<br/>

<p align="center">
  <sub>⚡ Constantly architecting the future of secure, resilient and high-throughput network infrastructure.</sub>
</p>