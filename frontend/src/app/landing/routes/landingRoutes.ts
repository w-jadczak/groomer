import LandingView from "@/app/landing/views/LandingView.vue"
import RegistrationView from "../views/RegistrationView.vue"

export default [
  {
    path: "/landing",
    name: "landing_view",
    component: LandingView,
  },
  {
    path: "/register",
    name: "registration_view",
    component: RegistrationView,
    meta: { title: "Registration" },
  },
]
