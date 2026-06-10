import { useState } from "react";
import { analyzeRepository } from "../api/workflowApi";
import Loader from "./Loader";
import "./RepositoryAnalyzer.css";

export default function RepositoryAnalyzer({
  onAnalysisComplete,
  onLoading,
}) {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [analysisData, setAnalysisData] = useState(null);

  const handleAnalyze = async () => {
    if (!repoUrl.trim()) {
      setError("Please enter a GitHub repository URL");
      return;
    }

    if (
      !repoUrl.includes("github.com") &&
      !repoUrl.includes("http") &&
      !repoUrl.includes("git")
    ) {
      setError("Please enter a valid GitHub repository URL");
      return;
    }

    setLoading(true);
    setError("");
    onLoading?.(true);

    try {
      const result = await analyzeRepository(repoUrl);

      if (result.status === "error") {
        setError(result.error || "Failed to analyze repository");
        return;
      }

      setAnalysisData(result);
      onAnalysisComplete?.(result);
    } catch (err) {
      setError(
        err.error || err.message || "Failed to analyze repository"
      );
    } finally {
      setLoading(false);
      onLoading?.(false);
    }
  };

  return (
    <div className="repository-analyzer">
      <div className="analyzer-card">
        <h2>Repository Analyzer</h2>
        <p className="subtitle">Analyze your GitHub repository to extract project structure and dependencies</p>

        <div className="input-group">
          <label>GitHub Repository URL</label>
          <input
            type="text"
            placeholder="https://github.com/username/repository"
            value={repoUrl}
            onChange={(e) => {
              setRepoUrl(e.target.value);
              setError("");
            }}
            disabled={loading}
            className={error ? "input-error" : ""}
          />
          {error && <span className="error-message">{error}</span>}
        </div>

        <button
          onClick={handleAnalyze}
          disabled={loading || !repoUrl.trim()}
          className="analyze-btn"
        >
          {loading ? (
            <>
              <Loader size={16} style={{ marginRight: "8px" }} />
              Analyzing...
            </>
          ) : (
            "Analyze Repository"
          )}
        </button>

        {analysisData && (
          <div className="analysis-results">
            <h3>Repository Summary</h3>
            <div className="results-grid">
              <div className="result-item">
                <span className="label">Project</span>
                <span className="value">
                  {analysisData.project_name || "Unknown"}
                </span>
              </div>
              <div className="result-item">
                <span className="label">Language</span>
                <span className="value">{analysisData.language || "N/A"}</span>
              </div>
              <div className="result-item">
                <span className="label">Framework</span>
                <span className="value">{analysisData.framework || "N/A"}</span>
              </div>
              <div className="result-item">
                <span className="label">Total Files</span>
                <span className="value">{analysisData.total_files || 0}</span>
              </div>
              {analysisData.api_endpoints && (
                <div className="result-item full-width">
                  <span className="label">API Endpoints</span>
                  <div className="endpoints-list">
                    {analysisData.api_endpoints.slice(0, 5).map((endpoint, idx) => (
                      <span key={idx} className="endpoint-tag">
                        {endpoint}
                      </span>
                    ))}
                    {analysisData.api_endpoints.length > 5 && (
                      <span className="endpoint-tag more">
                        +{analysisData.api_endpoints.length - 5} more
                      </span>
                    )}
                  </div>
                </div>
              )}
              {analysisData.dependencies && (
                <div className="result-item full-width">
                  <span className="label">Key Dependencies</span>
                  <div className="dependencies-list">
                    {analysisData.dependencies.slice(0, 5).map((dep, idx) => (
                      <span key={idx} className="dependency-tag">
                        {dep}
                      </span>
                    ))}
                    {analysisData.dependencies.length > 5 && (
                      <span className="dependency-tag more">
                        +{analysisData.dependencies.length - 5} more
                      </span>
                    )}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
