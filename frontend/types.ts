export interface ConnectRepositoryRequest {
  repository_id: string;
  external_processing_accepted: boolean;
}

export interface ConnectRepositoryResponse {
  job_id: string;
  status: "queued";
}
