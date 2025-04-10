# Serverless MLOps with GCP: Real-Time Inference Pipeline

This project demonstrates a scalable, low-latency MLOps pipeline using **GCP Pub/Sub**, **Vertex AI**, and **Cloud Functions**. Designed for real-time prediction use cases such as transaction classification, fraud detection, or user personalization.

---

## 🎯 Use Case

Example: A streaming ingestion service receives real-time events (e.g., credit card transactions), preprocesses them, and routes them through a deployed ML model hosted in Vertex AI.

---

## 🧱 Architecture

```plaintext
+-------------+      +------------------+     +--------------------+     +-------------------+
| Pub/Sub     | ---> | Cloud Function   | --> | Vertex AI Endpoint | --> | Prediction Output |
| Ingestion   |      | (Preprocessing)  |     | (Deployed Model)   |     | (BigQuery, Firestore, etc.)
+-------------+      +------------------+     +--------------------+     +-------------------+
