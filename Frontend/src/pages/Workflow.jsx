import { useState } from "react";
import RepositoryAnalyzer from "../components/RepositoryAnalyzer";
import TestCaseGenerator from "../components/TestCaseGenerator";
import AutomationGenerator from "../components/AutomationGenerator";
import ExecutionDashboard from "../components/ExecutionDashboard";
import "./Workflow.css";

export default function Workflow() {
  const [currentStep, setCurrentStep] = useState(1);
  const [repoContext, setRepoContext] = useState(null);
  const [testCases, setTestCases] = useState(null);
  const [automationCode, setAutomationCode] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const steps = [
    {
      id: 1,
      title: "Repository Analyzer",
      description: "Analyze GitHub repository",
    },
    {
      id: 2,
      title: "Test Generation",
      description: "Generate QA test cases",
    },
    {
      id: 3,
      title: "Automation Generation",
      description: "Generate automation code",
    },
    {
      id: 4,
      title: "Test Execution",
      description: "Run and monitor tests",
    },
  ];

  const handleRepositoryAnalyzed = (analysis) => {
    setRepoContext(analysis);
    setCurrentStep(2);
    window.scrollTo(0, 0);
  };

  const handleTestCasesGenerated = (testResult) => {
    setTestCases(testResult.test_cases);
    setCurrentStep(3);
    window.scrollTo(0, 0);
  };

  const handleAutomationGenerated = (automation) => {
    setAutomationCode(automation);
    setCurrentStep(4);
    window.scrollTo(0, 0);
  };

  const handleExecutionComplete = (result) => {
    // Execution complete - results displayed in dashboard
    window.scrollTo(0, 0);
  };

  const canProceed = (step) => {
    switch (step) {
      case 2:
        return !!repoContext;
      case 3:
        return !!testCases && testCases.length > 0;
      case 4:
        return !!automationCode;
      default:
        return true;
    }
  };

  const handleStepClick = (step) => {
    if (canProceed(step)) {
      setCurrentStep(step);
      window.scrollTo(0, 0);
    }
  };

  return (
    <div className="workflow-page">
      <div className="workflow-container">
        <div className="workflow-header">
          <h1>TestForge AI Workflow</h1>
          <p>
            Automate your QA testing: Analyze repositories → Generate test cases →
            Create automation code → Execute tests
          </p>
        </div>

        <div className="progress-tracker">
          <div className="steps-timeline">
            {steps.map((step, idx) => (
              <div key={step.id} className="timeline-item">
                <button
                  className={`step-node ${
                    currentStep === step.id
                      ? "active"
                      : currentStep > step.id
                        ? "completed"
                        : canProceed(step.id)
                          ? "available"
                          : "disabled"
                  }`}
                  onClick={() => handleStepClick(step.id)}
                  disabled={!canProceed(step.id) && currentStep !== step.id}
                >
                  {currentStep > step.id ? "✓" : step.id}
                </button>

                <div className="step-info">
                  <div className="step-title">{step.title}</div>
                  <div className="step-description">{step.description}</div>
                </div>

                {idx < steps.length - 1 && (
                  <div
                    className={`timeline-connector ${
                      currentStep > step.id ? "completed" : ""
                    }`}
                  />
                )}
              </div>
            ))}
          </div>
        </div>

        <div className="workflow-content">
          {currentStep === 1 && (
            <section className="step-section">
              <RepositoryAnalyzer
                onAnalysisComplete={handleRepositoryAnalyzed}
                onLoading={setIsLoading}
              />

              {!isLoading && !repoContext && (
                <div className="empty-state">
                  <div className="empty-icon">📦</div>
                  <h3>Start with Repository Analysis</h3>
                  <p>
                    Enter your GitHub repository URL to analyze its structure,
                    dependencies, and framework.
                  </p>
                </div>
              )}
            </section>
          )}

          {currentStep === 2 && (
            <section className="step-section">
              <TestCaseGenerator
                repoContext={repoContext}
                onGenerationComplete={handleTestCasesGenerated}
                onLoading={setIsLoading}
              />

              {!isLoading && !testCases && (
                <div className="empty-state">
                  <div className="empty-icon">📝</div>
                  <h3>Generate Test Cases</h3>
                  <p>
                    Write a user story to generate comprehensive QA test cases
                    including positive, negative, and edge case scenarios.
                  </p>
                </div>
              )}

              <div className="step-navigation">
                <button
                  className="nav-btn prev"
                  onClick={() => setCurrentStep(1)}
                >
                  ← Back
                </button>
                {testCases && testCases.length > 0 && (
                  <button
                    className="nav-btn next"
                    onClick={() => setCurrentStep(3)}
                  >
                    Next →
                  </button>
                )}
              </div>
            </section>
          )}

          {currentStep === 3 && (
            <section className="step-section">
              <AutomationGenerator
                repoContext={repoContext}
                testCases={testCases}
                onGenerationComplete={handleAutomationGenerated}
                onLoading={setIsLoading}
              />

              {!isLoading && !automationCode && (
                <div className="empty-state">
                  <div className="empty-icon">⚙️</div>
                  <h3>Generate Automation Code</h3>
                  <p>
                    Convert your test cases into executable automation code based
                    on your project's framework and language.
                  </p>
                </div>
              )}

              <div className="step-navigation">
                <button
                  className="nav-btn prev"
                  onClick={() => setCurrentStep(2)}
                >
                  ← Back
                </button>
                {automationCode && (
                  <button
                    className="nav-btn next"
                    onClick={() => setCurrentStep(4)}
                  >
                    Next →
                  </button>
                )}
              </div>
            </section>
          )}

          {currentStep === 4 && (
            <section className="step-section">
              <ExecutionDashboard
                generatedCode={automationCode}
                onExecutionComplete={handleExecutionComplete}
                onLoading={setIsLoading}
              />

              {!isLoading && !automationCode && (
                <div className="empty-state">
                  <div className="empty-icon">🚀</div>
                  <h3>Execute Tests</h3>
                  <p>
                    Run your generated automation tests and monitor results in
                    real-time.
                  </p>
                </div>
              )}

              <div className="step-navigation">
                <button
                  className="nav-btn prev"
                  onClick={() => setCurrentStep(3)}
                >
                  ← Back
                </button>
                <button
                  className="nav-btn reset"
                  onClick={() => {
                    setCurrentStep(1);
                    setRepoContext(null);
                    setTestCases(null);
                    setAutomationCode(null);
                  }}
                >
                  Start Over
                </button>
              </div>
            </section>
          )}
        </div>
      </div>
    </div>
  );
}
