{{- define "homelab-ai-platform.fullname" -}}
{{- default "homelab-ai-platform" .Release.Name -}}
{{- end -}}
