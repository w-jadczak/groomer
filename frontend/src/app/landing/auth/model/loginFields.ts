export const loginFields = [
  {
    name: "username",
    label: "Username",
    type: "text" as const,
    autocomplete: "username",
    required: true,
  },
  {
    name: "password",
    label: "Password",
    type: "password" as const,
    autocomplete: "current-password",
    required: true,
  },
]
