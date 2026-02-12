// AI Labs Portal - API Integration
// Server Configuration
const API_CONFIG = {
    baseURL: 'http://82.29.165.213:5000',
    timeout: 10000, // 10 seconds
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
};

// API Endpoints
const API_ENDPOINTS = {
    contact: '/api/contact',
    partnership: '/api/academy/partnership',
    careers: '/api/careers/apply',
    projects: '/api/projects',
    events: '/api/events'
};

/**
 * Generic API call function with error handling
 * @param {string} endpoint - API endpoint path
 * @param {object} options - Fetch options
 * @returns {Promise<object>} - Response data
 */
async function apiCall(endpoint, options = {}) {
    const url = API_CONFIG.baseURL + endpoint;
    const config = {
        ...options,
        headers: {
            ...API_CONFIG.headers,
            ...options.headers
        }
    };

    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), API_CONFIG.timeout);

        const response = await fetch(url, {
            ...config,
            signal: controller.signal
        });

        clearTimeout(timeoutId);

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || data.message || `HTTP Error: ${response.status}`);
        }

        return { success: true, data };
    } catch (error) {
        if (error.name === 'AbortError') {
            throw new Error('Request timeout. Please try again.');
        }
        throw error;
    }
}

/**
 * Submit contact form
 * @param {object} formData - Contact form data
 */
async function submitContactForm(formData) {
    return apiCall(API_ENDPOINTS.contact, {
        method: 'POST',
        body: JSON.stringify({
            name: formData.name,
            email: formData.email,
            type: formData.type || 'General Inquiry',
            message: formData.message
        })
    });
}

/**
 * Submit partnership request
 * @param {object} formData - Partnership form data
 */
async function submitPartnershipForm(formData) {
    return apiCall(API_ENDPOINTS.partnership, {
        method: 'POST',
        body: JSON.stringify({
            collegeName: formData.collegeName,
            email: formData.email,
            phone: formData.phone
        })
    });
}

/**
 * Submit job application
 * @param {object} formData - Career form data
 */
async function submitCareerForm(formData) {
    return apiCall(API_ENDPOINTS.careers, {
        method: 'POST',
        body: JSON.stringify({
            name: formData.name,
            email: formData.email,
            resumeLink: formData.resumeLink,
            coverLetter: formData.coverLetter,
            jobRole: formData.jobRole
        })
    });
}

/**
 * Fetch all projects
 */
async function getProjects() {
    return apiCall(API_ENDPOINTS.projects, {
        method: 'GET'
    });
}

/**
 * Add new project
 * @param {object} projectData - Project data
 */
async function addProject(projectData) {
    return apiCall(API_ENDPOINTS.projects, {
        method: 'POST',
        body: JSON.stringify(projectData)
    });
}

/**
 * Fetch all events
 */
async function getEvents() {
    return apiCall(API_ENDPOINTS.events, {
        method: 'GET'
    });
}

/**
 * Add new event
 * @param {object} eventData - Event data
 */
async function addEvent(eventData) {
    return apiCall(API_ENDPOINTS.events, {
        method: 'POST',
        body: JSON.stringify(eventData)
    });
}

/**
 * Show loading state on button
 * @param {HTMLElement} button - Button element
 * @param {boolean} loading - Loading state
 */
function setButtonLoading(button, loading) {
    if (loading) {
        button.dataset.originalText = button.textContent;
        button.disabled = true;
        button.textContent = 'Submitting...';
        button.style.opacity = '0.7';
    } else {
        button.disabled = false;
        button.textContent = button.dataset.originalText || button.textContent;
        button.style.opacity = '1';
    }
}

/**
 * Show notification message
 * @param {string} message - Message to display
 * @param {string} type - Type of message (success/error)
 */
function showNotification(message, type = 'success') {
    const icon = type === 'success' ? '✅' : '❌';
    alert(`${icon} ${message}`);
}

/**
 * Handle form submission with API integration
 * @param {HTMLFormElement} form - Form element
 * @param {Function} submitFunction - API submit function
 */
async function handleFormSubmit(form, submitFunction) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    const submitBtn = form.querySelector('button[type="submit"]');

    setButtonLoading(submitBtn, true);

    try {
        const result = await submitFunction(data);
        showNotification(result.data.message || 'Submitted successfully!', 'success');
        form.reset();
    } catch (error) {
        console.error('Form submission error:', error);
        showNotification(error.message || 'An error occurred. Please try again.', 'error');
    } finally {
        setButtonLoading(submitBtn, false);
    }
}

// Export for module usage (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        submitContactForm,
        submitPartnershipForm,
        submitCareerForm,
        getProjects,
        addProject,
        getEvents,
        addEvent,
        handleFormSubmit
    };
}
