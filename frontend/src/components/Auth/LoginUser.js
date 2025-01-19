import React, { useState } from "react";

const LoginUser = () => {
  const [isRegistering, setIsRegistering] = useState(false);
  const [isBusiness, setIsBusiness] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    phone: "",
    business_name: "",
  });

  // Handle input change
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Submit form to Flask backend
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (isRegistering && formData.password !== formData.confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    const userData = {
      name: formData.name,
      email: formData.email,
      password: formData.password,
      phone: formData.phone,
      is_business: isBusiness,
      business_name: isBusiness ? formData.business_name : null,
    };

    const response = await fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });

    const data = await response.json();
    alert(data.message);
  };

  return (
    <div className="container my-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card shadow p-4">
            <h2 className="text-center text-primary">
              {isRegistering ? "User Registration" : "User Login"}
            </h2>

            <form onSubmit={handleSubmit}>
              {isRegistering && (
                <>
                  <div className="mb-3">
                    <label className="form-label">Full Name</label>
                    <input
                      type="text"
                      name="name"
                      className="form-control"
                      onChange={handleChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Phone</label>
                    <input
                      type="text"
                      name="phone"
                      className="form-control"
                      onChange={handleChange}
                      required
                    />
                  </div>
                </>
              )}

              <div className="mb-3">
                <label className="form-label">Email</label>
                <input
                  type="email"
                  name="email"
                  className="form-control"
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Password</label>
                <input
                  type="password"
                  name="password"
                  className="form-control"
                  onChange={handleChange}
                  required
                />
              </div>

              {isRegistering && (
                <div className="mb-3">
                  <label className="form-label">Confirm Password</label>
                  <input
                    type="password"
                    name="confirmPassword"
                    className="form-control"
                    onChange={handleChange}
                    required
                  />
                </div>
              )}

              {isRegistering && (
                <>
                  <div className="mb-3">
                    <input
                      type="checkbox"
                      onChange={() => setIsBusiness(!isBusiness)}
                    />
                    <label className="ms-2">Register a Business</label>
                  </div>
                  {isBusiness && (
                    <div className="mb-3">
                      <label className="form-label">Business Name</label>
                      <input
                        type="text"
                        name="business_name"
                        className="form-control"
                        onChange={handleChange}
                        required
                      />
                    </div>
                  )}
                </>
              )}

              <button type="submit" className="btn btn-primary w-100">
                {isRegistering ? "Register" : "Login"}
              </button>
            </form>

            <button
              className="btn btn-link mt-3"
              onClick={() => setIsRegistering(!isRegistering)}
            >
              {isRegistering
                ? "Already have an account? Login"
                : "New user? Register here"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginUser;
