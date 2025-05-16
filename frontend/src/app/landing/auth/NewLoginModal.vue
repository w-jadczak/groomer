<script setup lang="ts">
import BaseModal from "@/common/components/base-modal/BaseModal.vue"
import ModalHeader from "@/app/landing/auth/components/ModalHeader.vue"
import GenericForm from "@/app/landing/auth/forms/GenericForm.vue"
import { loginFields } from "@/app/landing/auth/model/loginFields.ts"
import { login } from "@/app/landing/auth/api/useAuth.ts"

const isOpen = defineModel("is-open", { type: Boolean, default: false })

const onSubmit = async (data: Record<string, string>) => {
  await login(data.username, data.password)
  isOpen.value = false
}
</script>

<template>
  <BaseModal v-model:is-open="isOpen">
    <template #dialogPanel>
      <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <ModalHeader title="Sign in to your account" />

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <GenericForm :fields="loginFields" :on-submit="onSubmit">
            <template #extra>
              <div class="flex items-center justify-between">
                <div class="text-sm ml-auto">
                  <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">
                    Forgot password?
                  </a>
                </div>
              </div>
            </template>
          </GenericForm>

          <p class="mt-10 text-center text-sm/6 text-gray-500">
            Not a member?
            <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Join here!</a>
          </p>
        </div>
      </div>
    </template>
  </BaseModal>
</template>
