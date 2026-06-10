const keys = {
    repo: "testforge_repo_context",
    tests: "testforge_generated_tests",
    automation: "testforge_automation_code"
};

const read = (key, fallback = null)=>{
    try{
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : fallback;
    }
    catch(error){
        console.log(error);
        return fallback;
    }
};

const write = (key, value)=>{
    localStorage.setItem(
        key,
        JSON.stringify(value)
    );
};

export const saveRepoContext = (repoContext)=>{
    write(keys.repo, repoContext);
};

export const getRepoContext = ()=>{
    return read(keys.repo);
};

export const saveGeneratedTests = (tests)=>{
    write(keys.tests, tests);
};

export const getGeneratedTests = ()=>{
    return read(keys.tests, []);
};

export const saveAutomationCode = (automation)=>{
    write(keys.automation, automation);
};

export const getAutomationCode = ()=>{
    return read(keys.automation);
};
