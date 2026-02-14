/**
 * AI Labs Portal - Frontend API Service
 * 
 * INSTRUCTIONS:
 * 1. Add this file to your 'src/services' or 'assets/js' folder.
 * 2. Use the 'ApiService' object for all API calls.
 * 3. Use 'getImageUrl' helper for ALL <img> tags to fix path issues.
 */

const CONFIG = {
    BASE_URL: "https://apis.focsit.in",
    get API_URL() { return `${this.BASE_URL}/api`; }
};

/**
 * HELPER: Construct full image URL from relative path
 */
export const getImageUrl = (path) => {
    if (!path) return "https://via.placeholder.com/400x300?text=No+Image";
    if (path.startsWith('http')) return path;
    return `${CONFIG.BASE_URL}${path}`;
};

/**
 * CORE: Generic Fetch Wrapper
 */
async function request(endpoint, options = {}) {
    const url = endpoint.startsWith('http') ? endpoint : `${CONFIG.API_URL}${endpoint}`;
    const defaultHeaders = { 'Content-Type': 'application/json' };

    try {
        const response = await fetch(url, {
            ...options,
            headers: { ...defaultHeaders, ...options.headers }
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "API Error");
        return data;
    } catch (error) {
        console.error(`API Error [${endpoint}]:`, error);
        throw error;
    }
}

export const ApiService = {
    // Fetch Data
    getVacancies: () => request("/vacancies"),
    getProjects: () => request("/projects"),
    getProject: (idOrSlug) => request(`/projects/${idOrSlug}`),
    getEvents: () => request("/events"),
    getEvent: (idOrSlug) => request(`/events/${idOrSlug}`),

    // Submit Forms
    submitContact: (data) => request("/contact", {
        method: "POST",
        body: JSON.stringify(data)
    }),
    submitPartnership: (data) => request("/academy/partnership", {
        method: "POST",
        body: JSON.stringify(data)
    }),
    submitCareerApplication: (data) => request("/careers/apply", {
        method: "POST",
        body: JSON.stringify(data)
    })
};
