export const registerFields = [
  {
    name: "firstName",
    label: "First Name",
    type: "text" as const,
    required: true,
  },
  {
    name: "lastName",
    label: "Last Name",
    type: "text" as const,
    required: true,
  },
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
    required: true,
  },
  {
    name: "repeatPassword",
    label: "Repeat Password",
    type: "password" as const,
    required: true,
  },
  {
    name: "email",
    label: "E-mail",
    type: "email" as const,
    required: true,
  },
  {
    name: "mobile",
    label: "Mobile Number",
    type: "number" as const,
    required: true,
  },
]
