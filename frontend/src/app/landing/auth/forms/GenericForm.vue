<template>
  <form class="space-y-6" @submit.prevent="handleSubmit">
    <div v-for="field in fields" :key="field.name">
      <label :for="field.name" class="block text-sm/6 font-medium text-gray-900">{{
        field.label
      }}</label>
      <div class="mt-2">
        <input
          v-model="formData[field.name]"
          :id="field.name"
          :type="field.type"
          :autocomplete="field.autocomplete"
          :required="field.required"
          class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:outline-indigo-600 sm:text-sm/6"
        />
      </div>
    </div>

    <slot name="extra" />

    <button
      type="submit"
      class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500"
    >
      Submit
    </button>
  </form>
</template>
<script setup lang="ts">
import { reactive } from "vue"

const props = defineProps<{
  fields: {
    name: string
    label: string
    type: "text" | "password" | "email" | "number"
    autocomplete?: string
    required?: boolean
  }[]
  onSubmit: (data: Record<string, string>) => Promise<void>
}>()

const formData = reactive<Record<string, string>>({})
props.fields.forEach((f) => (formData[f.name] = ""))

const handleSubmit = async () => {
  await props.onSubmit({ ...formData })
}
</script>
