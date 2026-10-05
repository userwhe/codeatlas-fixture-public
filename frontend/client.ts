import type { ConnectRepositoryRequest, ConnectRepositoryResponse } from "./types";

export async function connectRepository(
  request: ConnectRepositoryRequest,
): Promise<ConnectRepositoryResponse> {
  const response = await fetch("/v1/repositories", {
    method: "POST",
    credentials: "same-origin",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });
  if (!response.ok) throw new Error(`Repository connection failed: ${response.status}`);
  return response.json() as Promise<ConnectRepositoryResponse>;
}
