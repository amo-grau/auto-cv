# Experience

Seeded from the existing CV and motivation letter, then extended in an interview
on 12.08.2026. Anything unconfirmed is tracked in `_gaps.md` — do not put it on a
CV until the owner confirms it.

## Robotics Software Engineer — Yaskawa Europe GmbH

- **When:** 09.2023 – Present
- **Where:** Munich, Germany
- **Tags:** c++, c#, python, ros, docker, grpc, jetson, jetson-orin, yaskawa-next,
  edge-ai, computer-vision, grasp-detection, object-detection,
  instance-segmentation, path-planning, collision-avoidance, ocr, halcon, onnx,
  pytorch, tdd, hexagonal-architecture, code-review, technical-leadership,
  mentoring, agile, industrial-robotics, cobots, palletizing, welding, trade-show

Official title is **Robotics Software Engineer**; no promotion since joining.
Confirmed 08.2026 — the old CV said "Backend robotics software developer" and the
letter said "Software Developer", both wrong.

### Ownership and technical leadership

Holds a senior's responsibilities without the senior title. Worth stating on a CV
as scope, not as rank.

- Owns **Pick Anything**, the trade-show pick-and-place application (below).
- Owns the vision-based AI software stack for training and deploying open-source
  AI models — the platform other applications build on.
- Reviews the code of around **4 developers across 4 projects**, and is the
  developer who merges to main on every project he works on. Not part of his
  formal job description. Named projects: a course preparation for learning
  Yaskawa NEXT, the Pick Anything fair cell, and an AI pipeline.
- Works to hexagonal architecture and teaches it to other developers on the team.

### Pick Anything — trade-show pick-and-place application

[Video](https://www.youtube.com/watch?v=cLZ84RRqHHs). AI-driven picking with
automatic path planning and collision avoidance, running in a Docker container on
an **NVIDIA Jetson Orin** embedded in the **Yaskawa NEXT** controller.

Built first for **Automatica 2025**, Munich.

Scope:

- Handles **more than 10 distinct object types** and retrains easily for more.
  Fruits and baskets as targets, wall blocks as obstacles to avoid.
- The user selects what to grasp; the system plans around everything else.

**Adoption — the strongest evidence on this CV:**

- Shipped to trade fairs across Europe.
- **Yaskawa USA built their own copy** to tour fairs in the United States.
- A third copy is being built for the German showroom, for customer demonstrations
  on site.
- Internally described as the most advanced cell Yaskawa has outside Japan.
  *Use that phrasing carefully — it is an internal assessment, not a published
  claim. The replication across regions is the fact; it speaks for itself.*

Measured performance:

- Instance segmentation inference: **40 ms**.
- Grasp candidate selection: **5 ms**.
- Collision environment generation and path planning: **500 ms**, run in parallel
  while the user selects the object to grasp, so it is not perceptible.
- **Grasp success rate above 95%, conditional on a path being found.** State the
  condition whenever the number is used — it is not a bare 95%.
- When a target sits too close to an obstacle no path is found; the application
  reports to the user *why* planning failed rather than failing silently.

### Vision-based AI platform

- Built the platform for training and deploying vision-based AI models: grasp
  detection, object detection and instance segmentation. Python, gRPC and ROS,
  deployed to NVIDIA Jetson boards in Docker containers.
- Built a Docker container that optimizes open-source AI model inference on
  NVIDIA Jetson boards, in Python and C++.

### Current project (under NDA)

**Disclosure settled 12.08.2026: the technologies may be named, the application may
not.** Write about the tools and the work; never about what it is used for, which
customer, or which product.

- Trains and deploys AI models for **OCR**.
- Uses **HALCON** for computer vision tasks.

Safe phrasing: "Training and deploying AI models for OCR, and computer vision work
with HALCON." Anything answering *what for* is out of bounds.

### Earlier work

- Designed and developed smart welding applications running on the Smart Pendant
  of Yaskawa collaborative robot arms, in C#, using Agile and Test-Driven
  Development.
- Worked on smart palletizing applications.

## Working Student, Chair for Neuro-prosthetics — TUM

- **When:** 04.2023 – 07.2023
- **Where:** Technical University of Munich, Munich, Germany
- **Tags:** c++, api-design, franka-emika, manipulators, trajectory-control,
  research, robotics

- Configured a Franka Emika Panda arm and wrote a C++ API that simplified
  trajectory control of the arm for other users in the lab.

## Working Student, Chair for Construction Robotics — TUM

- **When:** 03.2022 – 02.2023
- **Where:** Technical University of Munich, Munich, Germany
- **Tags:** ros, c++, python, plc, beckhoff, structured-text, ur10, manipulators,
  pick-and-place, industrial-automation, assembly

- Automated an industrial assembly process: programmed a pick-and-place routine
  for a UR10 manipulator driven by ROS (C++ and Python) together with a Beckhoff
  PLC (Structured Text).

## Supply Chain Intern — TRANE Technologies

- **When:** 03.2020 – 06.2020
- **Where:** Barcelona, Spain
- **Tags:** python, mysql, excel, data-analysis, manufacturing, quality, hvac

- Detected errors in the tests run on produced cooling machines by analysing the
  test result data, using Excel, Python and MySQL Server.
