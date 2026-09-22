+++
title = "Orphaned VMs for host-kernel live updates"
slug = "2026-09-22-orphaned-vms-linux-patches"
date = 2026-09-22T09:35:00+05:30
[taxonomies]
tags = ["systems"]
[extra]
source_url = "https://www.phoronix.com/news/Orphaned-VMs-Linux-Patches"
source_title = "Orphaned VMs: Running VMs Uninterrupted While Host Kernel Is Offline For Reboots/Updates"
source_type = "article"
newsletter_candidate = true
why_it_matters = "An early look at Linux/KVM work aimed at letting cloud VMs keep running while the host kernel is offline for live-update or reboot maintenance."
saved_link = "https://x.com/phoronix/status/2101999855564435617"
saved_title = "Phoronix sharing Orphaned VMs Linux patches"
related_url = "https://x.com/phoronix/status/2101999855564435617"
related_title = "Announcement post on X"
related_urls = ["https://lpc.events/event/20/contributions/2553/", "https://lore.kernel.org/all/20260920193650.3373435-1-pasha.tatashin@soleen.com/"]
related_titles = ["Linux Plumbers session: In-Kernel Caretaker for Orphaned VMs", "RFC patch series on lore.kernel.org"]
retrieval_note = "X post extracted via FXTwitter; Phoronix article and Linux Plumbers session page read directly. lore.kernel.org RFC pages were blocked by Anubis, so the primary patch text was not read directly."
+++

**Logged at IST:** 2026-09-22 09:35 IST

**What it is:** Phoronix coverage of experimental Linux/KVM RFC patches for “Orphaned VMs”: virtual machines that continue executing while their host kernel is offline for a live update or reboot.

**Gist:** The proposal comes from Pasha Tatashin and builds on Google's kexec-based Live Update Orchestrator. The idea is to keep guest execution alive on preserved, isolated physical CPUs while the host kernel and VMM are temporarily unavailable.

The key mechanism described in the Phoronix article and Linux Plumbers session is a “Caretaker”: a small bare-metal interpose layer running in privileged hypervisor state. During the reboot gap, it traps and handles some VM exits locally, while preserved `vcpufd` state, shielded CPUs, timekeeping, stray interrupts, and guest-to-guest IPIs have to be managed carefully enough that the VM survives the host-management gap.

This is still very early RFC work, reportedly tested across Intel, AMD, and Arm server processors, not production-ready. But it is a striking systems direction: cloud-maintenance pressure is pushing live update beyond “restart the host quickly” toward “the guest should barely notice that the host kernel disappeared.”

{{ tweet(id="2101999855564435617", url="https://x.com/phoronix/status/2101999855564435617") }}

**Newsletter angle:** Systems/virtualization item on how far hyperscaler zero-downtime maintenance pressure is pushing kernel/KVM live-update design.
