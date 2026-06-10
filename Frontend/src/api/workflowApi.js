import { api } from "./axios";

// Repository Analyzer API
export const analyzeRepository = async (repoUrl) => {
  try {
    const response = await api.post("/repository/analyze", {
      repo_url: repoUrl,
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Test Generation API
export const generateTestCases = async (repoContext, userStory, projectId = null) => {
  try {
    const response = await api.post("/tests/generate", {
      repo_context: repoContext,
      user_story: userStory,
      project_id: projectId,
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Automation Generation API
export const generateAutomation = async (repoContext, testCases, projectName = "TestProject") => {
  try {
    const response = await api.post("/automation/generate", {
      repo_context: repoContext,
      test_cases: testCases,
      project_name: projectName,
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Test Execution API
export const runTests = async (testFilePath, framework = null, timeout = 300) => {
  try {
    const response = await api.post("/tests/run", {
      test_file_path: testFilePath,
      framework: framework,
      timeout: timeout,
    });
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Get supported frameworks
export const getTestFrameworks = async () => {
  try {
    const response = await api.get("/tests/frameworks");
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Get automation frameworks
export const getAutomationFrameworks = async () => {
  try {
    const response = await api.get("/automation/frameworks");
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Get templates
export const getTestTemplates = async () => {
  try {
    const response = await api.get("/tests/templates");
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};

// Get generated files
export const getGeneratedFiles = async () => {
  try {
    const response = await api.get("/automation/generated-files");
    return response.data;
  } catch (error) {
    throw error.response?.data || error.message;
  }
};
